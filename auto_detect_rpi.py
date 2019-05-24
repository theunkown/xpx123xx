

# For every change brought to this file, don't forget to update its counterpart in DexterOS.

# RPI_VARIANTS was inspired from http://www.raspberrypi-spy.co.uk/2012/09/checking-your-raspberry-pi-board-version/
# This module is meant for retrieving the Raspberry Pi's generation model, PCB model (dimension-wise) and PCB revision
# Also check https://elinux.org/RPi_HardwareHistory for missing revision codes.
# Works with Python 3 & 2 !!!

# Each key represents the hardware revision number
# This isn't the same as the RaspberryPi revision
# Having the hardware revision number is useful when working with hardware or software.

RPI_VARIANTS = {
"0002" : ["Model B Rev v1.0", "RPI1"],

"0003" : ["Model B Rev v1.0 ECN0001 (no fuses, D14 removed)", "RPI1"],

"0004" : ["Model B Rev v2.0", "RPI1"],
"0005" : ["Model B Rev v2.0", "RPI1"],
"0006" : ["Model B Rev v2.0", "RPI1"],

"0007" : ["Model A v2.0", "RPI1"],
"0008" : ["Model A v2.0", "RPI1"],
"0009" : ["Model A v2.0", "RPI1"],

"000d" : ["Model B Rev v2.0", "RPI1"],
"000e" : ["Model B Rev v2.0", "RPI1"],
"000f" : ["Model B Rev v2.0", "RPI1"],

"0010" : ["Model B+ v1.2", "RPI1"],
"0013" : ["Model B+ v1.2", "RPI1"],
"900032" : ["Model B+ v1.2", "RPI1"],

"0011" : ["Compute Module v1.0", "RPI-COMPUTE-MODULE"],
"0014" : ["Compute Module v1.0", "RPI-COMPUTE-MODULE"],

"0012" : ["Model A+ v1.1", "RPI1"],
"0015" : ["Model A+ v1.1", "RPI1"],

"a01040" : ["Pi 2 Model B v1.0", "RPI2"],
    
"a01041" : ["Pi 2 Model B v1.1", "RPI2"],
"a21041" : ["Pi 2 Model B v1.1", "RPI2"],

"a22042" : ["Pi 2 Model B v1.2", "RPI2"],

"900092" : ["Pi Zero v1.2", "RPI0"],

"900093" : ["Pi Zero v1.3", "RPI0"],

"9000C1" : ["Pi Zero W v1.1", "RPI0"],

"a02082" : ["Pi 3 Model B v1.2", "RPI3"],
"a22082" : ["Pi 3 Model B v1.2", "RPI3"],
"a32082" : ["Pi 3 Model B v1.2", "RPI3"],
"a52082" : ["Pi 3 Model B v1.2", "RPI3"],
"a020d3" : ["Pi 3 Model B+ v1.3", "RPI3B+"],
"9020e0" : ["Pi 3 Model A+ v1.0", "RPI3A+"]
}

# represents indexes for each corresponding key in the above dictionary
RPI_MODEL_AND_PCBREV = 0
RPI_GENERATION_MODEL = 1

def getRPIHardwareRevCode():
    """
    Returns the hardware revision of the Raspberry Pi.
    If it can't find anything, it returns "NOT_FOUND".
    If there's an error while reading the file, it returns a None.
    Examples of strings returned : "Model B Rev 2", "Model A+", "Pi 3 Model B", etc.
    Look into the dictionary to see all the possible variants.
    """
    cpuinfo_lines = readLinesFromFile("/proc/cpuinfo")
    rpi_description = ""

    if not cpuinfo_lines is None:
        revision_line = cpuinfo_lines[-2]
        revision = revision_line.split(":")[-1]
        revision = revision.strip()

        if revision in RPI_VARIANTS.keys():
            rpi_description = RPI_VARIANTS[revision][RPI_MODEL_AND_PCBREV]
        else:
            rpi_description = "NOT_FOUND_" + revision

    return rpi_description

def getRPIGenerationCode():
    """
    Returns the Raspberry Pi's generation model.
    If it can't find anything, it returns "NOT_FOUND".
    If there's an error while reading the file, it returns a None.
    Depending on the Raspberry Pi's model, the function can return the following strings:
    "RPI0"
    "RPI1"
    "RPi2"
    "RPI3"
    "RPI-COMPUTE-MODULE"
    """

    cpuinfo_lines = readLinesFromFile("/proc/cpuinfo")
    rpi_description = ""

    if not cpuinfo_lines is None:
        revision_line = cpuinfo_lines[-2]
        revision = revision_line.split(":")[-1]
        revision = revision.strip()

        if revision in RPI_VARIANTS.keys():
            rpi_description = RPI_VARIANTS[revision][RPI_GENERATION_MODEL]
        else:
            rpi_description = "NOT_FOUND_" + revision

    return rpi_description

def readLinesFromFile(filename):
    """
    Returns the read file as a list of strings.
    Each element of the list represents a line.
    On error it returns None.
    """
    try:
        with open(filename, "r") as input_file:
            lines = input_file.readlines()
        return lines

    except EnvironmentError:
        return None
