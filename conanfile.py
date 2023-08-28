from conan import ConanFile
from conan.errors import ConanInvalidConfiguration
from conan.tools.cmake import CMakeToolchain, CMake, cmake_layout
from conan.tools.files import collect_libs, copy, get, apply_conandata_patches, export_conandata_patches, mkdir, rename
from conan.tools.microsoft import is_msvc_static_runtime, is_msvc
import os

required_conan_version = ">=1.60.0"

class SimpleCmake(ConanFile):
    name = "simple-cmake"
    description = "Simple cmake project"
    topics = ("cmake")
    url = "https://github.com/conan-io/conan-center-index"
    homepage = ""
    license = "MIT"
    settings = "os", "arch", "compiler", "build_type"
    package_type = "library"

    options = {
        "shared": [True, False],
        "fPIC": [True, False],
    }
    default_options = {
        "shared": False,
        "fPIC": True,
    }

    def export_sources(self):
        copy(self, "*", os.path.join(self.recipe_folder, "src"), os.path.join(self.export_sources_folder, "src"), excludes=["cmake-*", "conan", ".conan"])

    def layout(self):
        cmake_layout(self, src_folder="src")

    def config_options(self):
        if self.settings.os == "Windows":
            del self.options.fPIC

    def configure(self):
        if self.options.shared:
            self.options.rm_safe("fPIC")

    def generate(self):
        tc = CMakeToolchain(self)
        tc.generate()

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        #cmake.build(target="LibA")
        #cmake.build(target="LibB")
        cmake.build(target="LibC")

    def package(self):
        copy(self, "libLibC.a", src=os.path.join(self.build_folder, "LibC"), dst=os.path.join(self.package_folder, "lib"), keep_path=False)
        copy(self, "libLibC.so", src=os.path.join(self.build_folder, "LibC"), dst=os.path.join(self.package_folder, "lib"), keep_path=False)

        if is_msvc(self):
            if self.options.shared:
                copy(self, "LibC.dll", src=os.path.join(self.build_folder, "LibC", f"{self.settings.build_type}"), dst=os.path.join(self.package_folder, "lib"), keep_path=False)
            else:
                copy(self, "LibC.lib", src=os.path.join(self.build_folder, "LibC", f"{self.settings.build_type}"), dst=os.path.join(self.package_folder, "lib"), keep_path=False)

        copy(self, "*.h", src=os.path.join(self.source_folder, "LibC", "include"), dst=os.path.join(self.package_folder, "include"))

    def package_info(self):
        if self.settings.os == "Windows" and self.options.shared:
            self.cpp_info.bindirs.append("lib")
        else:
            self.cpp_info.libs = ["LibC"]
