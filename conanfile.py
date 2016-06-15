from conans import ConanFile, CMake, tools
import os


class dateConan(ConanFile):
    """ contains ONLY the date and iso_week header only.
    The TZ library will be handled in a separate package
    """
    name = "date"
    version = "1.0.0"
    license = "MIT"
    url = "https://github.com/memsharded/conan-date"

    def source(self):
       self.run("git clone https://github.com/HowardHinnant/date")
       self.run("cd date && git checkout v1.0.0")

    def package(self):
        self.copy("*date.h", dst="include", src="date")
        self.copy("*iso_week.h", dst="include", src="date")
