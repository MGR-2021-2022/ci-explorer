from typing import TypedDict

from metrics.calculations.FailedTests.Condition import Condition
from metrics.calculations.FailedTests.conditions.EqualCondition import EqualCondition
from metrics.calculations.FailedTests.conditions.ListCondition import ListCondition
from metrics.calculations.FailedTests.conditions.RangeCondition import RangeCondition
from metrics.calculations.FailedTests.measures.InspectionTime import InspectionTime
from metrics.calculations.FailedTests.measures.InspectionType import InspectionType
from metrics.calculations.FailedTests.measures.IsAuthor import IsAuthor
from metrics.calculations.FailedTests.measures.SourceCodeLinesChanged import SourceCodeLinesChanged
from metrics.calculations.FailedTests.measures.Technology import Technology
from metrics.calculations.FailedTests.measures.TestCodeLinesChanged import TestCodeLinesChanged
from metrics.calculations.FailedTests.measures.UserCommitNumber import UserCommitNumber


class Group:
    def __init__(self, label: str, condition: Condition):
        self.label = label
        self.condition = condition

class GroupsFactory:

    def getInspectionTypeGroups(self):
        measure = InspectionType()

        return [

            Group("Build", ListCondition(measure, [
                #VSCODE
                "VS Code", "VS Code (macOS macOS)", "VS Code (Windows Windows)", "VS Code (Linux Linuxx64)",
                "VS Code (Compile Compile)", "VS Code (LinuxServerDependencies x64)", "richnav", "VS Code (macOS macOSUniversalSign)",
                "VS Code (macOS macOSSign)", "VS Code (macOS macOSUniversal)", "VS Code (Windows Windows32)", "VS Code (Linux LinuxSnap)",
                "VS Code (macOS macOSARM64Sign)", "VS Code (Windows WindowsARM64)", "VS Code (Linux LinuxArmhf)", "VS Code (macOS macOSARM64)",
                "VS Code (Linux LinuxArm64)", "VS Code (Linux LinuxAlpineArm64)", "VS Code (Linux LinuxWeb)", "VS Code (Linux LinuxAlpine)",
                "VS Code (Release Release Build)", "VS Code (Linux Linux)", "VS Code (Compile Hygiene)", "VS Code (Linux LinuxSnapArm64)",
                "VS Code (Linux LinuxSnapArmhf)", "VS Code (macOS_universal macOSUniversal)", "VS Code (Compile Windows)",
                "VS Code (macOSARM64 macOSARM64)", "Build: Compile Core", "Build: Compile Extensions", "VS Code (Mooncake)",
                "VS Code (Compile)", "VS Code (LinuxSnap)", "VS Code (macOS)", "VS Code (LinuxAlpine)", "VS Code (LinuxArmhf)",
                "VS Code (LinuxWeb)", "VS Code (LinuxArm64)", "VS Code (WindowsARM64)", "VS Code (Windows)",
                "VS Code (Windows32)", "VS Code (Linux)", "VS Code (Mooncake macOS)", "microsoft.vscode", "microsoft.vscode (macOS)",
                "VS Code (Publish Publish Build)", "VS Code (Release Release Build)", "VS Code (Publish Sync Mooncake)",
                "VS Code (Publish Release Build)", "VS Code (Publish Build Service)",  "VS Code (Release macOS)",
                "VS Code (Publish LinuxSnap)", "VS Code (Publish Build Service (Mooncake))", "VS Code (Release)",
                #DJANGO
                "Trigger Full Build (main)",
                #BITCOIN
                "ARM64 Android APK [focal]", "macOS 10.15 [gui, no tests] [focal]", "macOS 10.14 [gui, no tests] [focal]",
                "x86_64 Linux  [GOAL: install]  [bionic]  [Using ./ci/ system]", "FreeBsd 12.0 amd64  [GOAL: install]  [no depends, only system libs]",
                "x86_64 Linux  [GOAL: install]  [bionic]  [C++17, previous releases, uses qt5 dev package and some depends packages] [unsigned char]",
                "x86_64 Linux  [GOAL: install]  [focal]  [depends, sanitizers: memory (MSan)]", "x86_64 Linux [GOAL: install]  [focal]  [multiprocess]",
                "x86_64 Linux  [GOAL: install]  [focal]  [depends, sanitizers: thread (TSan), no gui]", "macOS 10.12  [GOAL: deploy] [no functional tests]",
                "macOS 10.15 [gui, no tests] [focal 20.04]", "ARM64 Android APK [focal 20.04]", "Win64  [GOAL: deploy]  [unit tests, no gui, no boost::process, no functional tests]",
                "ARM  [GOAL: install]  [buster]  [unit tests, no functional tests]", "Win64 [installer]", "macOS 10.15 native [gui] [no depends]",
                "ARM64 Android APK [bionic]", "macOS 10.14 [gui, no tests] [bionic]", "[no depends, sanitizers: fuzzer,address,undefined] [focal]",
                "macOS 10.15 native [GOAL: install] [GUI] [no depends]", "x86_64 Linux  [GOAL: install]  [bionic]  [no wallet]",
                "x86_64 Linux  [GOAL: install]  [bionic]  [previous releases, uses qt5 dev package and some depends packages] [unsigned char]",
                "32-bit + dash  [GOAL: install]  [CentOS 8]  [gui]", "macOS 10.14  [GOAL: deploy] [no functional tests]",
                "x86_64 Linux  [GOAL: install]  [focal]  [no depends, only system libs, fuzzers under valgrind]", "FreeBsd 12.1 amd64  [GOAL: install]  [no depends, only system libs]",
                "x86_64 Linux  [GOAL: install]  [bionic]  [no depends, only system libs, sanitizers: address/leak (ASan + LSan) + undefined (UBSan) + integer]",
                #LEXICAL
                "integrity (16.x)", "integrity (16.8)", "integrity (12.x)", "build (12.x)", "build (10.x)",
                #TERRAFORM
                "Build for darwin_arm64", "Build for darwin_amd64", "Build for windows_amd64", "Build for windows_386",
                "Build for solaris_amd64", "Build for openbsd_amd64", "Build for openbsd_386", "Build for linux_arm64",
                "Build for linux_arm", "Build for linux_amd64", "Build for linux_386", "Build for freebsd_arm",
                "Build for freebsd_amd64", "Build for freebsd_386",
                # LARAVEL
                #DEVILUTION_X
                "build", "ps4", "testflow", "Travis CI - Pull Request", "Travis CI - Branch",
                #FLUTTER
                "Linux fuchsia_precache", "Linux flutter_plugins", "Build Parsing Results", "docker_build",
                "build-ipas+drive-examples PLUGIN_SHARDING:--shardIndex 1 --shardCount 4",
                "build-ipas+drive-examples PLUGIN_SHARDING:--shardIndex 3 --shardCount 4",
                "build-ipas+drive-examples PLUGIN_SHARDING:--shardIndex 0 --shardCount 4",
                "build-ipas+drive-examples PLUGIN_SHARDING:--shardIndex 2 --shardCount 4",
                "Mac build_gallery", "Linux build_gallery", "Build",
                #STARSHIP
                "Compile with all features enabled", "Compile with no features enabled", "Compile",
                "notarize_and_pkgbuild (aarch64-apple-darwin, aarch64, starship-aarch64-apple-darwin.tar.gz, stars...",
                "notarize_and_pkgbuild (x86_64-apple-darwin, x86_64, starship-x86_64-apple-darwin.tar.gz, starship...",
                "Build release binaries (x86_64-unknown-freebsd, ubuntu-latest, starship-x86_64-unknown-freebsd.ta...",
                "Build release binaries (aarch64-pc-windows-msvc, windows-latest, starship-aarch64-pc-windows-msvc...",
                "Build release binaries (i686-pc-windows-msvc, windows-latest, starship-i686-pc-windows-msvc.zip)",
                "Build release binaries (x86_64-pc-windows-msvc, windows-latest, starship-x86_64-pc-windows-msvc.zip)",
                "Build release binaries (aarch64-apple-darwin, macOS-11, starship-aarch64-apple-darwin.tar.gz)",
                "Build release binaries (x86_64-apple-darwin, macOS-11, starship-x86_64-apple-darwin.tar.gz)",
                "Build release binaries (arm-unknown-linux-musleabihf, ubuntu-latest, starship-arm-unknown-linux-m...",
                "Build release binaries (aarch64-unknown-linux-musl, ubuntu-latest, starship-aarch64-unknown-linux...",
                "Build release binaries (i686-unknown-linux-musl, ubuntu-latest, starship-i686-unknown-linux-musl....",
                "Build release binaries (x86_64-unknown-linux-musl, ubuntu-latest, starship-x86_64-unknown-linux-m...",
                "Build release binaries (x86_64-unknown-linux-gnu, ubuntu-latest, starship-x86_64-unknown-linux-gn...",
                "Build release binaries (aarch64-apple-darwin, macOS-latest, starship-aarch64-apple-darwin.tar.gz)",
                "Build release binaries (x86_64-apple-darwin, macOS-latest, starship-x86_64-apple-darwin.tar.gz)",
                "Build release binaries", "Build release binaries (x86_64-pc-windows-msvc)", "Build release binaries (x86_64-apple-darwin)",
                "Build release binaries (x86_64-unknown-linux-musl)", "Build release binaries (x86_64-unknown-linux-gnu)",
                "matchai.starship",
                #CBL-MARINER
                "Build",

            ])),

            Group("Build related", ListCondition(measure, [
                # VSCODE
                "VS Code Distro Sync & Merge Check",
                "VS Code (Upload Configuration for Bing Upload Configuration for Bing)", "VS Code (Mooncake Sync Mooncake)", "Generate cache image",
                # DJANGO
                "docs",
                # BITCOIN
                "Build Parsing Results",
                # LEXICAL
                # TERRAFORM
                "backport", "merge_job", "Generate release metadata",
                "Build documentation bundle", "Determine intended Terraform version",
                # LARAVEL
                "update", "update / update",
                # DEVILUTION_X
                "fmt-check", "prebuild",
                # FLUTTER
                "docs-linux", "linux_docs", "Linux docs", "docs", "Windows docs",
                "Prebuild dev/ci/docker_linux/Dockerfile",
                "Linux web_benchmarks_html", "Mac_ios hot_mode_dev_cycle_macos_target__benchmark",
                "Linux_android hot_mode_dev_cycle_linux__benchmark", ".github/dependabot.yml",
                "Linux benchmark web_benchmarks_html", "linux_web_benchmarks_html", "deploy_gallery",
                # STARSHIP
                "Dprint [Docs Formatter]", "Publish docs to Netlify", "Publish Cargo Package", "Check if config schema is up to date",
                "Block Translated Changes", "Mixed content", "Redirect rules", "Header rules", "Pages changed", "Mixed content - starship-rs",
                "Redirect rules - starship-rs", "Header rules - starship-rs", "Pages changed - starship-rs", "Update Brew Formula",
                "Update Homebrew Formula",
                # CBL-MARINER

            ])),



            Group("Tests", ListCondition(measure, [
                # VSCODE
                "Windows", "Linux", "Monaco Editor checks", "macOS", "Notebook random action tests", "Monaco Editor", "monaco",
                "Build: Linux Unit Tests", "Build: macOS Integration Tests", "Build: Linux Integration Tests",
                "Build: macOS Unit Tests", "Build: macOS Smoke Tests", "Build: macOS Node Modules", "Notebook random action tests (Linux)",
                "Notebook random action tests (Windows)", "darwin", ".github/workflows/ci.yml",
                # DJANGO
                "Windows, SQLite, Python 3.11.0-alpha - 3.11.0", "Windows, SQLite, Python 3.10",
                "Windows, SQLite, Python 3.9", "Windows, SQLite, Python 3.8", "JavaScript tests",
                # BITCOIN
                "Win64 native [msvc]", "32-bit + dash [gui] [CentOS 8]", "[previous releases, uses qt5 dev package and some depends packages, DEBUG] [unsigned char] [buster]", 
                "[no wallet, libbitcoinkernel] [bionic]", "Win64 [unit tests, no gui tests, no boost::process, no functional tests] [jammy]", 
                "macOS 12 native [gui, system sqlite only] [no depends]", "ARM [unit tests, no functional tests] [buster]", 
                "[multiprocess, DEBUG] [focal]", "Win64 [unit tests, no gui tests, no boost::process, no functional tests] [focal]", 
                "[no wallet] [bionic]", "[previous releases, uses qt5 dev package and some depends packages, DEBUG] [unsigned char] [bionic]", 
                "macOS 11 native [gui, sqlite only] [no depends]", "Win64 [unit tests, no gui tests, no boost::process, no functional tests] [focal 20.04]", 
                "Win64 native [unit tests, no functional tests] [msvc]", "[multiprocess] [focal]", 
                "x86_64 Linux  [GOAL: install]  [focal]  [no depends, only system libs, sanitizers: fuzzer,address,undefined]", 
                "x86_64 Linux  [GOAL: install]  [focal]  [no depends, only system libs, sanitizers: address/leak (ASan + LSan) + undefined (UBSan) + integer]", 
                "[previous releases, uses qt5 dev package and some depends packages] [unsigned char] [bionic]", 
                "Win64 [unit tests, no gui tests, no boost::process, no functional tests] [bionic]", 
                "S390x  [GOAL: install]  [buster]  [unit tests, functional tests]", "Win64  [GOAL: deploy]  [unit tests, no gui tests, no boost::process, no functional tests]", 
                # LEXICAL
                "e2e-collab-windows (16.8, chromium)", "e2e-windows (16.8, firefox, plain-text, modern-events)", 
                "e2e-windows (16.8, firefox, plain-text, legacy-events)", "e2e-windows (16.8, firefox, rich-text, modern-events)", 
                "e2e-windows (16.8, firefox, rich-text, legacy-events)", "e2e-windows (16.8, chromium, plain-text, modern-events)", 
                "e2e-windows (16.8, chromium, plain-text, legacy-events)", "e2e-windows (16.8, chromium, rich-text, modern-events)",
                "e2e-windows (16.8, chromium, rich-text, legacy-events)", "e2e-collab-mac (16.8, chromium)", "unit (16.8)",
                "e2e-mac (16.8, webkit, plain-text, modern-events)", "e2e-mac (16.8, webkit, rich-text, modern-events)",
                "e2e-mac (16.8, webkit, rich-text, legacy-events)", "e2e-mac (16.8, firefox, plain-text, modern-events)",
                "e2e-mac (16.8, firefox, plain-text, legacy-events)", "e2e-mac (16.8, firefox, rich-text, modern-events)",
                "e2e-mac (16.8, firefox, rich-text, legacy-events)", "e2e-mac (16.8, chromium, plain-text, modern-events)",
                "e2e-mac (16.8, chromium, plain-text, legacy-events)", "e2e-mac (16.8, chromium, rich-text, modern-events)",
                "e2e-mac (16.8, chromium, rich-text, legacy-events)", "e2e-linux (16.8, firefox, plain-text, modern-events)",
                "e2e-linux (16.8, firefox, plain-text, legacy-events)", "e2e-linux (16.8, firefox, rich-text, modern-events)",
                "e2e-linux (16.8, firefox, rich-text, legacy-events)", "e2e-linux (16.8, chromium, plain-text, modern-events)",
                "e2e-linux (16.8, chromium, plain-text, legacy-events)", "e2e-linux (16.8, chromium, rich-text, modern-events)",
                "e2e-linux (16.8, chromium, rich-text, legacy-events)", "e2e-windows (16.8, firefox, plain-text, false)",
                "e2e-windows (16.8, firefox, rich-text, false)", "e2e-windows (16.8, chromium, plain-text, false)",
                "e2e-windows (16.8, chromium, rich-text, false)", "e2e-mac (16.8, webkit, plain-text, false)",
                "e2e-mac (16.8, webkit, rich-text, false)", "e2e-mac (16.8, firefox, plain-text, false)",
                "e2e-mac (16.8, firefox, rich-text, false)", "e2e-mac (16.8, chromium, plain-text, false)",
                "e2e-mac (16.8, chromium, rich-text, false)", "e2e-linux (16.8, firefox, plain-text, false)",
                "e2e-linux (16.8, firefox, rich-text, false)", "e2e-linux (16.8, chromium, plain-text, false)",
                "e2e-linux (16.8, chromium, rich-text, false)", "e2e-mac (16.8, webkit, plain-text)", "e2e-mac (16.8, firefox, plain-text)",
                "e2e-mac (16.8, firefox, rich-text)", "e2e-mac (16.8, chromium, rich-text)", "e2e-windows (16.8, firefox, plain-text)",
                "e2e-windows (16.8, chromium, plain-text)", "e2e-windows (16.8, chromium, rich-text)", "e2e-linux (16.8, firefox, rich-text)",
                "e2e-linux (16.8, chromium, plain-text)", "e2e-linux (16.x, firefox, plain-text)", "e2e-linux (16.x, chromium, plain-text)",
                "e2e-linux (16.x, chromium, rich-text)", "e2e-mac (16.x, webkit, rich-text)", "e2e-mac (16.x, firefox, plain-text)",
                "e2e-mac (16.x, chromium, plain-text)", "e2e-mac (16.x, chromium, rich-text)", "e2e-windows (16.x, firefox, rich-text)",
                "e2e-windows (16.x, chromium, plain-text)", "e2e-mac (16.x, firefox)", "e2e-linux (16.x, chromium)", "e2e-windows (16.x, firefox)",
                "e2e-firefox-mac (16.x)", "e2e-firefox-windows (16.x)", "e2e-chromium-mac (16.x)", "e2e-chromium-linux (16.x)", "e2e (16.x)",
                "e2e-chromium-ubuntu (16.x)",  "e2e-webkit-macos (16.x)",  "e2e-firefox-ubuntu (16.x)",  "e2e (12.x)",
                # TERRAFORM
                "End-to-end Tests", "Unit Tests", "Cloud End-to-end Tests", "e2etest for windows_amd64",
                "e2etest for linux_amd64", "Build e2etest for linux_amd64", "Build e2etest for windows_amd64",
                "Build e2etest for darwin_amd64", "e2etest for darwin_amd64",
                # LARAVEL
                "PostgreSQL 14", "MariaDB 10", "PHP 8.1 - prefer-stable", "MySQL 8.0", "PHP 8.1 - prefer-lowest",
                "MySQL 5.7", "PHP 8.0 - prefer-stable", "PHP 8.0 - prefer-lowest", "PHP 8.0 - prefer-stable - Windows",
                "PHP 8.0 - prefer-lowest - Windows", "PHP 7.4 - prefer-stable - Windows",
                "PHP 7.4 - prefer-lowest - Windows",
                "PHP 7.3 - prefer-stable - Windows", "PHP 7.3 - prefer-lowest - Windows", "PHP 7.4 - prefer-stable",
                "PHP 7.4 - prefer-lowest", "PHP 7.3 - prefer-stable", "PHP 7.3 - prefer-lowest",
                "PHP 8.1 - prefer-lowest - Windows",
                "SQL Server 2019", "PHP 8.1 - prefer-stable - Windows", "PHP 7.2 - prefer-stable",
                "PHP 7.2 - prefer-lowest",
                "PHP 7.2 - prefer-stable - Windows", "PHP 7.2 - prefer-lowest - Windows",
                "PHP 8 - prefer-stable - Windows",
                "PHP 8 - prefer-lowest - Windows", "PHP 8 - prefer-stable", "PHP 8 - prefer-lowest",
                "P7.4 - Sprefer-stable",
                "P7.4 - Sprefer-lowest", "P7.3 - Sprefer-stable", "P7.3 - Sprefer-lowest", "P7.2 - Sprefer-stable",
                "P7.2 - Sprefer-lowest",
                # DEVILUTION_X
                # FLUTTER
                "web_smoke_test", "framework_tests-widgets-linux", "framework_tests-misc-linux", "customer_testing-linux",
                "framework_tests-libraries-linux", "Linux web_canvaskit_tests_3", "Linux web_long_running_tests_4_5",
                "Windows build_tests_1_3", "Linux web_tests_0", "Mac customer_testing", "Linux web_canvaskit_tests_0",
                "Linux web_tests_6", "Windows framework_tests_misc", "Windows build_tests_3_3", "Linux web_canvaskit_tests_5",
                "Linux web_tests_2", "Linux web_canvaskit_tests_4", "Linux web_tests_1", "Linux web_canvaskit_tests_2",
                "Mac framework_tests_widgets", "Windows customer_testing", "Linux web_canvaskit_tests_6", "Linux web_tests_7_last",
                "Mac build_tests_3_4", "Linux web_long_running_tests_5_5", "Linux web_tests_3", "Linux framework_tests_misc",
                "Linux web_canvaskit_tests_7_last", "Linux web_long_running_tests_1_5", "Mac build_tests_4_4",
                "Mac build_tests_2_4", "Linux deferred components", "Linux web_tests_5", "Linux android views",
                "Mac build_tests_1_4", "Mac framework_tests_misc", "Windows framework_tests_widgets",
                "Linux firebase_android_embedding_v2_smoke_test", "Linux web_canvaskit_tests_1", "Linux web_long_running_tests_2_5",
                "Mac framework_tests_libraries", "Linux framework_tests_libraries", "Linux framework_tests_widgets",
                "Linux web_tests_4", "Windows build_tests_2_3", "Mac tool_tests_commands", "Linux build_tests_1_2",
                "Windows framework_tests_libraries", "Linux firebase_release_smoke_test", "Linux web_long_running_tests_3_5",
                "Linux customer_testing", "Linux build_tests_2_2", "Linux docs_test", "Linux firebase_abstract_method_smoke_test",
                "Windows web_tool_tests", "Windows tool_tests_general", "Windows tool_tests_commands",
                "Windows tool_integration_tests_6_6", "Windows tool_integration_tests_5_6", "Windows tool_integration_tests_4_6",
                "Windows tool_integration_tests_3_6", "Windows tool_integration_tests_2_6", "Windows tool_integration_tests_1_6",
                "Windows plugin_test", "Windows plugin_dependencies_test", "Windows module_test", "Windows module_host_with_custom_build_test",
                "Windows module_custom_host_app_name_test", "Windows gradle_plugin_bundle_test", "Windows build_aar_module_test",
                "Mac run_release_test_macos", "Mac native_ui_tests_macos", "Mac web_tool_tests", "Mac tool_tests_general",
                "Mac tool_integration_tests_4_4", "Mac tool_integration_tests_3_4", "Mac tool_integration_tests_2_4",
                "Mac tool_integration_tests_1_4", "Mac plugin_test_ios", "Mac plugin_test", "Mac plugin_dependencies_test",
                "Mac module_test_ios", "Mac module_test", "Mac module_host_with_custom_build_test",
                "Mac module_custom_host_app_name_test", "Mac gradle_plugin_fat_apk_test", "Mac gradle_plugin_bundle_test",
                "Mac dart_plugin_registry_test", "Mac build_ios_framework_module_test", "Mac build_aar_module_test",
                "Linux web_tool_tests", "Linux tool_tests_general", "Linux tool_tests_commands", "Linux tool_integration_tests_4_4",
                "Linux tool_integration_tests_3_4", "Linux tool_integration_tests_2_4", "Linux tool_integration_tests_1_4",
                "Linux plugin_test", "Linux plugin_dependencies_test", "Linux module_test", "Linux module_host_with_custom_build_test",
                "Linux module_custom_host_app_name_test", "Linux gradle_plugin_light_apk_test", "Linux gradle_plugin_fat_apk_test",
                "Linux gradle_plugin_bundle_test", "Linux gradle_java8_compile_test", "Linux gradle_desugar_classes_test",
                "Linux build_aar_module_test", "tool_tests-general-linux", "tool_tests-commands-linux",
                "framework_tests_widgets", "framework_tests_misc", "win_framework_tests_libraries", "win_customer_testing",
                "win_build_tests_3_3", "win_build_tests_2_3", "win_build_tests_1_3", "mac_framework_tests_widgets",
                "mac_framework_tests_misc", "mac_framework_tests_libraries", "mac_customer_testing", "mac_build_tests_4_4",
                "mac_build_tests_3_4", "mac_build_tests_2_4", "mac_build_tests_1_4", "web_long_running_tests_5_5",
                "web_long_running_tests_4_5", "web_long_running_tests_3_5", "web_long_running_tests_2_5",
                "web_long_running_tests_1_5", "linux_web_tests_7_last", "linux_web_tests_6", "linux_web_tests_5",
                "linux_web_tests_4", "linux_web_tests_3", "linux_web_tests_2", "linux_web_tests_1", "linux_web_tests_0",
                "web_tests4-5-linux", "web_tests5-7_last-linux", "web_tests5-2-linux", "web_tests6-1-linux",
                "web_tests4-6-linux", "web_tests7-1-linux", "web_tests7-3-linux", "web_tests6-3-linux", "web_tests5-4-linux",
                "web_tests7-5-linux", "web_tests6-5-linux", "web_tests4-3-linux", "web_tests7-7_last-linux",
                "web_tests6-6-linux", "web_tests6-2-linux", "web_tests5-5-linux", "web_tests8-2-linux",
                "web_tests4-4-linux", "web_tests6-7_last-linux", "web_tests5-1-linux", "web_tests8-1-linux",
                "web_tests7-0-linux", "web_tests8-4-linux", "web_tests4-2-linux", "web_tests2-3-linux",
                "web_tests5-3-linux", "web_tests4-7_last-linux", "web_tests4-1-linux", "web_tests3-2-linux",
                "web_tests5-0-linux", "web_tests1-5-linux", "web_tests8-5-linux", "web_tests1-4-linux",
                "web_tests1-1-linux", "web_tests7-4-linux", "web_tests8-6-linux", "web_tests3-0-linux",
                "web_tests4-0-linux", "web_tests6-4-linux", "web_tests8-3-linux", "web_tests3-4-linux",
                "web_tests8-0-linux", "web_tests1-3-linux", "web_tests5-6-linux", "web_tests3-7_last-linux",
                "web_tests6-0-linux", "web_tests2-4-linux", "web_tests2-6-linux", "web_tests3-3-linux",
                "web_tests7-6-linux", "web_tests8-7_last-linux", "web_tests2-2-linux", "web_tests3-5-linux",
                "web_tests1-7_last-linux", "web_tests2-1-linux", "web_tests7-2-linux", "web_tests2-7_last-linux", "web_tests3-1-linux",
                "web_tests2-0-linux", "web_tests3-6-linux", "web_tests2-5-linux", "web_tests1-0-linux", "web_tests1-6-linux",
                "web_tests1-2-linux", "web_tests9-6-linux", "web_tests9-1-linux", "web_tests9-5-linux", "web_tests9-2-linux",
                "web_tests9-0-linux", "web_tests9-4-linux", "web_tests9-3-linux", "web_tests9-7_last-linux", "web_tests02-0-linux",
                "web_tests03-0-linux", "web_tests03-7_last-linux", "web_tests03-4-linux", "web_tests01-3-linux", "web_tests01-7_last-linux",
                "web_tests03-6-linux", "web_tests02-7_last-linux", "web_tests02-6-linux", "web_tests03-5-linux", "web_tests01-0-linux",
                "web_tests04-0-linux", "web_tests03-3-linux", "web_tests02-4-linux", "web_tests02-5-linux", "web_tests01-1-linux",
                "web_tests02-1-linux", "web_tests03-1-linux", "web_tests01-5-linux", "web_tests01-6-linux", "web_tests01-4-linux",
                "web_tests02-2-linux", "web_tests05-4-linux", "web_tests04-6-linux", "web_tests04-2-linux", "web_tests04-7_last-linux",
                "web_tests05-7_last-linux", "web_tests05-1-linux", "web_tests05-6-linux", "web_tests04-1-linux", "web_tests05-5-linux",
                "web_tests04-4-linux", "web_tests05-3-linux", "web_tests03-2-linux", "web_tests04-3-linux", "web_tests05-0-linux",
                "web_tests02-3-linux", "web_tests01-2-linux", "web_tests05-2-linux", "web_tests04-5-linux", "web_tests06-2-linux",
                "web_tests07-0-linux", "web_tests13-5-linux", "web_tests07-4-linux", "web_tests06-5-linux", "web_tests08-4-linux",
                "web_tests12-7_last-linux", "web_tests12-0-linux", "web_tests12-1-linux", "web_tests08-1-linux", "web_tests10-6-linux",
                "web_tests10-5-linux", "web_tests11-2-linux", "web_tests09-3-linux", "web_tests09-1-linux", "web_tests13-7_last-linux",
                "web_tests09-6-linux", "web_tests10-1-linux", "web_tests12-6-linux", "web_tests10-4-linux", "web_tests13-0-linux",
                "web_tests06-7_last-linux", "web_tests07-1-linux", "web_tests08-0-linux", "web_tests06-6-linux", "web_tests10-7_last-linux",
                "web_tests14-3-linux", "web_tests07-3-linux", "web_tests06-4-linux", "web_tests09-7_last-linux", "web_tests08-6-linux",
                "web_tests10-0-linux", "web_tests11-3-linux", "web_tests08-7_last-linux", "web_tests08-2-linux", "web_tests13-4-linux",
                "web_tests09-2-linux", "web_tests10-3-linux", "web_tests13-3-linux", "web_tests13-2-linux", "web_tests09-4-linux",
                "web_tests07-7_last-linux", "web_tests11-5-linux", "web_tests07-6-linux", "web_tests09-0-linux", "web_tests14-1-linux",
                "web_tests06-3-linux", "web_tests11-1-linux", "web_tests14-0-linux", "web_tests07-2-linux", "web_tests11-7_last-linux",
                "web_tests13-6-linux", "web_tests10-2-linux", "web_tests09-5-linux", "web_tests13-1-linux", "web_tests11-4-linux",
                "web_tests08-3-linux", "web_tests12-3-linux", "web_tests12-4-linux", "web_tests12-5-linux", "web_tests12-2-linux",
                "web_tests14-2-linux", "web_tests14-7_last-linux", "web_tests07-5-linux", "web_tests06-1-linux", "web_tests14-5-linux",
                "web_tests08-5-linux", "web_tests11-6-linux", "web_tests15-4-linux", "web_tests15-6-linux", "web_tests15-3-linux",
                "web_tests15-0-linux", "web_tests06-0-linux", "web_tests11-0-linux", "web_tests15-1-linux", "web_tests15-7_last-linux",
                "web_tests15-5-linux", "web_tests14-4-linux", "web_tests14-6-linux", "web_tests15-2-linux", "web_tests27-6-linux",
                "web_tests29-7_last-linux", "web_tests25-1-linux", "web_tests30-6-linux", "web_tests20-2-linux", "web_tests30-5-linux",
                "web_tests27-3-linux", "web_tests29-0-linux", "web_tests26-0-linux", "web_tests29-3-linux", "web_tests28-7_last-linux",
                "web_tests26-5-linux", "web_tests17-7_last-linux", "web_tests29-4-linux", "web_tests27-2-linux", "web_tests26-2-linux",
                "web_tests26-3-linux", "web_tests19-6-linux", "web_tests20-4-linux", "web_tests20-5-linux", "web_tests20-0-linux",
                "web_tests29-2-linux", "web_tests25-2-linux", "web_tests18-2-linux", "web_tests28-5-linux", "web_tests18-4-linux",
                "web_tests19-1-linux", "web_tests18-0-linux", "web_tests28-6-linux", "web_tests30-3-linux", "web_tests28-3-linux",
                "web_tests24-5-linux", "web_tests28-0-linux", "web_tests21-1-linux", "web_tests19-4-linux", "web_tests25-7_last-linux",
                "web_tests26-6-linux", "web_tests27-4-linux", "web_tests29-1-linux", "web_tests24-6-linux", "web_tests28-2-linux",
                "web_tests25-0-linux", "web_tests30-0-linux", "web_tests28-1-linux", "web_tests30-1-linux", "web_tests25-5-linux",
                "web_tests20-1-linux", "web_tests29-5-linux", "web_tests19-3-linux", "web_tests24-7_last-linux", "web_tests27-0-linux",
                "web_tests18-1-linux", "web_tests21-2-linux", "web_tests27-1-linux", "web_tests22-7_last-linux", "web_tests25-6-linux",
                "web_tests25-3-linux", "web_tests23-1-linux", "web_tests30-4-linux", "web_tests19-0-linux", "web_tests17-2-linux",
                "web_tests24-1-linux", "web_tests30-2-linux", "web_tests22-1-linux", "web_tests24-0-linux", "web_tests30-7_last-linux",
                "web_tests17-1-linux", "web_tests28-4-linux", "web_tests24-2-linux", "web_tests21-5-linux", "web_tests27-7_last-linux",
                "web_tests16-2-linux", "web_tests22-3-linux", "web_tests20-3-linux", "web_tests23-7_last-linux", "web_tests18-3-linux",
                "web_tests23-3-linux", "web_tests23-4-linux", "web_tests23-5-linux", "web_tests26-7_last-linux", "web_tests23-2-linux",
                "web_tests22-5-linux", "web_tests26-1-linux", "web_tests20-7_last-linux", "web_tests21-6-linux", "web_tests19-5-linux",
                "web_tests22-0-linux", "web_tests27-5-linux", "web_tests29-6-linux", "web_tests16-5-linux", "web_tests16-7_last-linux",
                "web_tests25-4-linux", "web_tests18-5-linux", "web_tests21-0-linux", "web_tests16-6-linux", "web_tests26-4-linux",
                "web_tests22-2-linux", "web_tests20-6-linux", "web_tests22-6-linux", "web_tests16-3-linux", "web_tests18-6-linux",
                "web_tests24-4-linux", "web_tests21-3-linux", "web_tests16-4-linux", "web_tests19-2-linux", "web_tests17-5-linux",
                "web_tests23-6-linux", "web_tests23-0-linux", "web_tests18-7_last-linux", "web_tests19-7_last-linux",
                "web_tests17-3-linux", "web_tests17-4-linux", "web_tests24-3-linux", "web_tests21-4-linux", "web_tests22-4-linux",
                "web_tests17-0-linux", "web_tests16-1-linux", "web_tests21-7_last-linux", "web_tests16-0-linux", "web_tests17-6-linux",
                "customer_testing-windows", "hostonly_devicelab_tests-3_last-windows", "hostonly_devicelab_tests-0-macos",
                "add_to_app_tests-macos", "hostonly_devicelab_tests-1-windows", "customer_testing-macos", "framework_tests-libraries-macos",
                "build_tests-1_last-windows", "build_tests-0-macos", "framework_tests-widgets-macos", "hostonly_devicelab_tests-0-windows",
                "tool_tests-general-macos", "hostonly_devicelab_tests-1-macos", "web_tests-6-linux", "build_tests-0-linux",
                "hostonly_devicelab_tests-2-macos", "framework_tests-misc-macos", "web_tests-7_last-linux", "build_tests-1_last-macos",
                "tool_tests-integration-macos", "build_tests-0-windows", "hostonly_devicelab_tests-2-windows", "web_tests-0-linux",
                "tool_tests-commands-windows", "tool_tests-integration-windows", "hostonly_devicelab_tests-2-linux",
                "tool_tests-commands-macos", "hostonly_devicelab_tests-3_last-macos", "integration_tests_gradle2-windows",
                "tool_tests_commands-windows", "web_tests-linux-shard-2", "bots_tests-windows", "tool_tests_commands-linux",
                "web_tests-linux-shard-1", "tool_tests_general-windows", "web_tests-linux-shard-0", "tool_tests_general-macos",
                "bots_tests-macos", "tool_tests_general-linux", "tool_tests_commands-macos", "bots_tests-linux",
                "web_tests-5_last-linux", "web_tests-linux-shard-5", "web_tests-linux-shard-4", "web_tests-linux-shard-3",
                "hostonly_devicelab_tests-3-linux", "hostonly_devicelab_tests-4-linux", "hostonly_devicelab_tests-5_last-windows",
                "hostonly_devicelab_tests-5_last-macos", "hostonly_devicelab_tests-4-macos", "hostonly_devicelab_tests-5_last-linux",
                "hostonly_devicelab_tests-3-windows", "hostonly_devicelab_tests-4-windows", "hostonly_devicelab_tests-3-macos",
                "tests_framework_other-macos", "tests_widgets-macos", "gradle_tests-linux-shard-1", "gradle_embedding_v2_tests-linux-shard-1",
                "gradle_embedding_v2_tests-linux-shard-2", "gradle_embedding_v2_tests-windows-shard-2", "gradle_tests-windows-shard-1",
                "gradle_tests-linux-shard-2", "gradle_tests-windows-shard-2", "gradle_embedding_v2_tests-windows-shard-1",
                "debug_smoke_tests", "tests_extras-macos", "tool_tests_integration-macos", "web_tests-macos", "web_tests-windows",
                "Mac_android run_release_test", "Linux test_ownership", "Windows tool_integration_tests_5_5", "Windows tool_integration_tests_3_5",
                "Windows tool_integration_tests_4_5", "Windows tool_integration_tests_2_5", "Windows gradle_plugin_light_apk_test",
                "Mac gradle_plugin_light_apk_test", "Windows tool_integration_tests_1_5", "linux_firebase_release_smoke_test",
                "linux_firebase_android_embedding_v2_smoke_test", "linux_firebase_abstract_method_smoke_test", "linux_framework_tests_widgets",
                "linux_framework_tests_misc", "linux_framework_tests_libraries", "linux_build_tests_2_2", "linux_build_tests_1_2",
                "linux_customer_testing", "web_tests-4-linux", "web_tests-2-linux", "firebase_test_lab_tests-1-linux",
                "web_integration_tests", "deploy_gallery-macos", "hostonly_devicelab_tests-3_last-linux", "firebase_test_lab_tests-2_last-linux",
                "build_tests-1_last-linux", "framework_tests-libraries-windows", "tool_tests-integration-linux", "web_tests-5-linux",
                "hostonly_devicelab_tests-1-linux", "framework_tests-misc-windows", "web_tests-3-linux", "hostonly_devicelab_tests-0-linux",
                "web_tests-1-linux", "framework_tests-widgets-windows", "firebase_test_lab_tests-0-linux", "tool_tests-general-windows",
                "Windows tool_tests", "Windows framework_tests", "Windows build_tests", "Linux web_smoke_test", "Linux web_integration_tests",
                "Linux web_tests", "Linux tool_tests", "Linux hostonly_devicelab_tests", "Linux framework_tests", "Linux build_tests",
                "Windows tool_integration_tests", "Windows gradle_non_android_plugin_test", "Mac tool_integration_tests",
                "Mac tool_tests", "Mac gradle_non_android_plugin_test", "Mac framework_tests", "Mac build_tests",
                "Linux web_e2e_test", "Linux web_long_running_tests", "Linux tool_integration_tests", "Linux gradle_non_android_plugin_test",
                "Windows tool_integration_tests_3_3", "Windows tool_integration_tests_2_3", "Windows tool_integration_tests_1_3",
                "Mac tool_integration_tests_3_3", "Mac tool_integration_tests_2_3", "Mac tool_integration_tests_1_3",
                "Linux web_long_running_tests_3_3", "Linux web_long_running_tests_2_3", "Linux web_long_running_tests_1_3",
                "Linux tool_integration_tests_3_3", "Linux tool_integration_tests_2_3", "Linux tool_integration_tests_1_3",
                "linux_gradle_plugin_light_apk_test", "win_tool_integration_tests_4_5", "win_module_test", "tool_tests_general",
                "win_web_tool_tests", "linux_tool_integration_tests_2_4", "mac_module_host_with_custom_build_test",
                "linux_plugin_test", "linux_module_custom_host_app_name_test", "mac_tool_integration_tests_4_4",
                "mac_tool_tests_general", "mac_plugin_lint_mac", "mac_web_tool_tests", "mac_build_ios_framework_module_test",
                "mac_build_aar_module_test", "win_module_host_with_custom_build_test", "mac_plugin_test", "win_tool_integration_tests_1_5",
                "mac_gradle_plugin_light_apk_test", "mac_tool_integration_tests_1_4", "win_tool_integration_tests_3_5",
                "mac_tool_integration_tests_2_4", "win_tool_integration_tests_2_5", "mac_module_test", "win_build_aar_module_test",
                "win_plugin_test", "win_tool_integration_tests_5_5", "linux_web_tool_tests", "linux_tool_tests_commands",
                "tool_tests_commands", "linux_module_host_with_custom_build_test", "win_gradle_plugin_bundle_test",
                "linux_tool_integration_tests_3_4", "mac_module_custom_host_app_name_test", "mac_gradle_plugin_fat_apk_test",
                "win_module_custom_host_app_name_test", "dart_plugin_registry_test", "linux_module_test", "mac_gradle_plugin_bundle_test",
                "linux_tool_tests_general", "linux_tool_integration_tests_1_4", "mac_module_test_ios", "win_gradle_plugin_light_apk_test",
                "linux_tool_integration_tests_4_4", "mac_tool_integration_test_3_4", "linux_gradle_desugar_classes_test",
                "linux_gradle_plugin_fat_apk_test", "linux_gradle_plugin_bundle_test", "linux_build_aar_module_test",
                "Windows tool_integration_tests_4_4", "Windows tool_integration_tests_3_4", "Windows tool_integration_tests_2_4",
                "Windows tool_integration_tests_1_4", "build_tests-windows", "build_tests-linux", "build_tests-macos",
                "firebase_test_lab_tests-linux", "Linux gradle_r8_test", "Mac macos_content_validation_test", "tests-windows",
                "integration_tests-windows", "tests-macos", "integration_tests-macos", "tool_tests-macos", "tool_tests-windows",
                "integration_tests-linux", "tool_tests-linux", "tests-linux", "Mac ios_content_validation_test", "testonly_devicelab_tests",
                "Windows gradle_r8_test", "Windows gradle_jetifier_test", "Windows gradle_fast_starttest", "Mac gradle_r8_test",
                "Mac gradle_jetifier_test", "Mac gradle_fast_start_test", "Linux gradle_jetifier_test", "Linux gradle_fast_start_test",
                "web_tests-8-linux", "web_tests-11_last-linux", "web_tests-9-linux", "web_tests-10-linux", "web_tests-7-linux",
                "hostonly_devicelab_tests-1_last-windows", "firebase_test_lab_tests-2-linux", "codelabs-build-test",
                "android_packaging_tests-linux", "tool_tests_create-windows", "integration_tests_gradle1-windows",
                "web_tests-linux", "tests_widgets-windows", "integration_tests_gradle1-linux", "tests_extras-windows",
                "tests_framework_other-windows", "integration_tests_gradle2-linux", "tests_framework_other-linux",
                "tests_widgets-linux", "tests_extras-linux", "release_smoke_tests", "tool_tests_integration-windows",
                "tool_tests_integration-linux", "tool_tests_create-linux", "tool_tests_create-macos", "integration_tests_gradle2-macos",
                "framework_tests_misc-macos", "framework_tests_widgets-macos", "integration_tests_misc-macos", "integration_tests_gradle1-macos",
                "framework_tests_widgets-windows", "framework_tests_libraries-windows", "integration_tests_misc-windows",
                "framework_tests_libraries-macos", "framework_tests_widgets-linux", "framework_tests_misc-windows",
                "release_smoke_tests-linux", "integration_tests_misc-linux", "framework_tests_misc-linux", "framework_tests_libraries-linux",
                "tool_tests-macos SHARD_INDEX:1 SUBSHARD:tool", "aot_build_tests-linux", "tool_tests_1-windows", "tool_tests_2-windows",
                "tool_tests_1-macos", "tool_tests_2-macos", "tool_tests_1-linux", "tool_tests_2-linux", "tool_tests_coverage-linux",
                "integration_tests_android-linux", "integration_tests_android-windows", "integration_tests_agradle-linux",
                "integration_tests_gradle-linux", "plugins-ios-integration-tests PLUGIN_SHARDING:--shardIndex 3 --shardCount 4",
                "plugins-ios-integration-tests PLUGIN_SHARDING:--shardIndex 0 --shardCount 4",
                "plugins-ios-integration-tests PLUGIN_SHARDING:--shardIndex 2 --shardCount 4",
                "plugins-ios-integration-tests PLUGIN_SHARDING:--shardIndex 1 --shardCount 4",
                "tool_tests_0-linux", "tool_tests_4-linux", "tool_tests_5-linux", "tool_tests_3-linux",
                # STARSHIP
                "Starship Test Suite", "Starship Test Suite (Test Docker test)", "Starship Test Suite (Test Cargo test stable MacOS)",
                "Starship Test Suite (Test Cargo test stable Linux)", "Starship Test Suite (Test Cargo test nightly Linux)",
                "Starship Test Suite (Checks Cargo check)", "Starship Test Suite (Checks Check rustfmt)", "Starship Test Suite (Checks Run linter)",
                "test (macOS-latest, nightly)", "test (macOS-latest, stable)", "test (ubuntu-latest, nightly)", "docker_test",
                "test (ubuntu-latest, stable)", "Starship Test Suite (Docker test)", "Starship Test Suite (Cargo test nightly Linux)",
                "Starship Test Suite (Cargo test stable MacOS)", "Starship Test Suite (Cargo test stable Linux)", "Starship Test Suite (Cargo check)",
                "Starship Test Suite (Check rustfmt)", "Starship Test Suite (Run linter)", "Starship Test Suite (Check starship with nightly)",
                "Starship Test Suite (Test starship Docker)", "Starship Test Suite (Test starship MacOS)", "Starship Test Suite (Test starship Linux)",
                "Starship Test Suite (Cargo test stable Windows)", "Starship Test Suite (Cross check and test)", "Starship Test Suite (Test starship Windows)",
                "Starship Test Suite (Run integration test within Docker)", "Starship Test Suite (Test linux-nightly)",
                "Starship Test Suite (Test linux-beta)", "Starship Test Suite (Test linux-stable)", "Starship Test Suite (Test mac-stable)",
                "Starship Test Suite (Test windows-stable)", "Starship Test Suite (Rustfmt)", "Starship Test Suite (Docker)",
                "Starship Test Suite (Clippy)", "Starship Test Suite (Test)", "Starship Test Suite (Run dockerized integration tests)",
                "Starship Test Suite (Docker_tests)", "Starship Test Suite (Bench)", "matchai.starship (Test linux-nightly)",
                "matchai.starship (Test linux-beta)", "matchai.starship (Test linux-stable)", "matchai.starship (Test mac-stable)",
                "matchai.starship (Test windows-stable)", "Test Suite (windows-latest, nightly)", "Test Suite (windows-latest, stable)",
                "Test Suite (macOS-latest, nightly)", "Test Suite (macOS-latest, stable)", "Test Suite (ubuntu-latest, nightly)",
                "Test Suite (ubuntu-latest, stable)", "Test in Docker", "Test Suite",
                # CBL-MARINER
                "Spec %clean stage check",
                "Spec files check",
            ])),

            Group("Code quality", ListCondition(measure, [
                # VSCODE
                "Hygiene, Layering and Monaco Editor", "VS Code Scan", "VS Code Scan (Windows WindowsJob)", "VS Code Scan (Linux LinuxJob)",
                "Hygiene and Layering", "Analyze (csharp)", "Analyze (java)", "Analyze (go)", "Analyze (python)",
                "Analyze (cpp)", "Analyze (javascript)", "Hygiene and Layers check",
                # DJANGO
                "isort", "flake8", "black",
                # BITCOIN
                "lint [bionic]", "tidy [jammy]", "[fuzzer,address,undefined,integer, no depends] [focal]",
                "[fuzzer,address,undefined,integer, no depends] [jammy]", "lint",
                "[no depends, sanitizers: fuzzer,address,undefined,integer] [focal 20.04]",
                # LEXICAL
                # TERRAFORM
                "CodeQL", "Code Consistency Checks", "codecov/patch", "codecov/project",
                # LARAVEL
                "Types", "Source Code", "PHP 8.0", "PHP 8.1",
                # DEVILUTION_X
                "codecov/project", "formatting-check", "Formatting Check (test)", "Formatting Check (Source)",
                # FLUTTER
                "tool_coverage-linux", "upload_coverage", "tool_coverage_a-linux", "tool_coverage_upload",
                "tool_coverage_b-linux", "analyze", "Linux analyze", "linux_analyze",
                # STARSHIP
                "codecov/patch", "codecov/project", "Clippy [Linter] (windows-latest)", "Clippy [Linter] (macOS-latest)",
                "Clippy [Linter] (ubuntu-latest)", "Clippy [Linter]", "Rustfmt [Formatter]", "clippy", "rustfmt", "Clippy (Linter)",
                "Rustfmt (Formatter)", "matchai.starship (Rustfmt)", "matchai.starship (Clippy)",
                # CBL-MARINER
                "Go Test Coverage", "Spec Linting", "spec-lint", "Check Spec for version and/or release update and parsing",
                "Spec Entanglement Mismatch Check",
            ])),

            Group("Vulnerabilites", ListCondition(measure, [
                # VSCODE
                "CodeQL", "1CS Compliance", "CodeQL-Build",
                # DJANGO
                # BITCOIN
                "[depends, sanitizers: memory (MSan)] [focal]", "[depends, sanitizers: thread (TSan), no gui] [hirsute]",
                "[no depends, sanitizers: address/leak (ASan + LSan) + undefined (UBSan) + integer] [hirsute]",
                "[no depends, sanitizers: fuzzer,address,undefined,integer] [focal]", "[TSan, depends, no gui] [jammy]",
                "[no depends, sanitizers: address/leak (ASan + LSan) + undefined (UBSan) + integer] [jammy]",
                "[no depends, sanitizers: address/leak (ASan + LSan) + undefined (UBSan) + integer] [hirsute 21:04]",
                "[depends, sanitizers: memory (MSan)] [focal 20.04]", "[depends, sanitizers: thread (TSan), no gui] [focal]",
                "[depends, sanitizers: thread (TSan), no gui] [hirsute 21:04]", "[ASan + LSan + UBSan + integer, no depends] [jammy]",
                "[MSan, depends] [focal]", "[depends, sanitizers: thread (TSan), no gui] [jammy]", "[TSan, depends, gui] [jammy]",
                "[no depends, sanitizers: address/leak (ASan + LSan) + undefined (UBSan) + integer] [focal]",
                "[no depends, only system libs, sanitizers: fuzzer,address,undefined] [focal]",
                "[no depends, only system libs, sanitizers: address/leak (ASan + LSan) + undefined (UBSan) + integer] [focal]",
                # LEXICAL
                # TERRAFORM
                # LARAVEL
                # DEVILUTION_X
                # FLUTTER
                "analyze-linux",
                # STARSHIP
                "security_audit", "Cargo Audit [Security]", "cargo_check", "Security audit",
                # CBL-MARINER
                "parameterized-cve-scan-with-patch-info-github",
            ])),

            Group("Package management", ListCondition(measure, [
                # VSCODE
                "Build Error", "Prevent yarn.lock changes in PRs",
                # DJANGO
                # BITCOIN
                # LEXICAL
                # TERRAFORM
                "Determine Go toolchain version", "Go Modules Scanner",
                # LARAVEL
                # DEVILUTION_X
                "Build Error",
                # FLUTTER
                # STARSHIP
                # CBL-MARINER
                "Check Manifests", "Check Package CGManifests", "Validate Manifests",
            ])),

            Group("Policy management", ListCondition(measure, [
                # VSCODE
                ".github/workflows/needs-version-info.yml",
                # DJANGO
                "Hello new contributor",
                # BITCOIN
                # LEXICAL
                "Facebook CLA Check",
                # TERRAFORM
                # LARAVEL
                # DEVILUTION_X
                # FLUTTER
                "cla/google",
                # STARSHIP
                # CBL-MARINER
                "Spec License Map Check",
            ])),

            Group("Github management", ListCondition(measure, [
                # VSCODE
                # DJANGO
                # BITCOIN
                # LEXICAL
                # TERRAFORM
                ".github/dependabot.yml",
                # LARAVEL
                "uneditable",
                # DEVILUTION_X
                # FLUTTER
                "WIP",
                # STARSHIP
                "auto-merge", "Create GitHub Release", "Auto-merge Dependabot PRs",
                # CBL-MARINER
            ])),

            Group("Unrecognized", ListCondition(measure, [
                # VSCODE
                "main", ".github/workflows/commands.yml", ".github/workflows/copycat.yml", "VS Code Exploration Sync", "VS Code (Job)",
                # DJANGO
                # BITCOIN
                "Build Failed",
                # LEXICAL
                # TERRAFORM
                # LARAVEL
                # DEVILUTION_X
                # FLUTTER
                "Linux skp_generator", "ci.yaml validation", "Windows windows_home_scroll_perf__timeline_summary",
                "Mac plugin_lint_mac", "Linux ci_yaml flutter roller", "Scorecard", "Windows home_scroll_perf__timeline_summary",
                "flutter_plugins", "linux_skp_generator", "linux_fuchsia_precache", "verify_binaries_codesigned-macos",
                "deploy_gallery-linux", "fuchsia_precache-linux", "Windows", "Linux", "noResponse", "Scorecards analysis",
                "lock", "Linux validate_ci_config", "Linux deferred_components", "Linux android_views", "add2app-macos",
                "main", "gold_tryjob_status", "add_to_app-macos", "markdown_link_check",
                # STARSHIP
                "Create AUR release",
                # CBL-MARINER
            ])),
        ]

    def getInspectionTimeGroups(self):
        measure = InspectionTime()
        return [
            Group("0-10", RangeCondition(measure, 0, 10)),
            Group("10-20", RangeCondition(measure, 10, 20)),
            Group("20-30", RangeCondition(measure, 20, 30)),
            Group("30-40", RangeCondition(measure, 30, 40)),
            Group("40-50", RangeCondition(measure, 40, 50)),
            Group("50-60", RangeCondition(measure, 50, 60)),
            Group("60-90", RangeCondition(measure, 60, 90)),
            Group("90-180", RangeCondition(measure, 90, 180)),
            Group("180-720", RangeCondition(measure, 180, 720)),
            Group("720-999999", RangeCondition(measure, 720, 999999))
        ]

    def getIsAuthorGroups(self):
        measure = IsAuthor()
        return [
            Group("Author", EqualCondition(measure, True)),
            Group("Not author", EqualCondition(measure, False))
        ]

    def getUserCommitNumberGroups(self):
        measure = UserCommitNumber()
        return [
            Group("0-10", RangeCondition(measure, 0, 10)),
            Group("10-50", RangeCondition(measure, 10, 50)),
            Group("50-100", RangeCondition(measure, 50, 100)),
            Group("100-300", RangeCondition(measure, 100, 300)),
            Group("300-500", RangeCondition(measure, 300, 500)),
            Group("500-700", RangeCondition(measure, 500, 700)),
            Group("700-1200", RangeCondition(measure, 700, 1200)),
            Group("1200-2000", RangeCondition(measure, 1200, 2000)),
            Group("2000-999999", RangeCondition(measure, 2000, 999999))
        ]

    def getTechnologyGroups(self):
        measure = Technology()
        return [
            Group("TypeScript", EqualCondition(measure, "TypeScript")),
            Group("Python", EqualCondition(measure, "Python")),
            Group("C++", EqualCondition(measure, "C++")),
            Group("JavaScript", EqualCondition(measure, "JavaScript")),
            Group("Go", EqualCondition(measure, "Go")),
            Group("PHP", EqualCondition(measure, "PHP")),
            Group("Dart", EqualCondition(measure, "Dart")),
            Group("Rust", EqualCondition(measure, "Rust")),
        ]

    def getSourceCodeLinesChanged(self):
        measure = SourceCodeLinesChanged()
        return [
            Group("0", RangeCondition(measure, 0, 1)),
            Group("1-10", RangeCondition(measure, 1, 10)),
            Group("10-30", RangeCondition(measure, 10, 30)),
            Group("30-50", RangeCondition(measure, 30, 50)),
            Group("50-100", RangeCondition(measure, 50, 100)),
            Group("100-200", RangeCondition(measure, 100, 200)),
            Group("200-500", RangeCondition(measure, 200, 500)),
            Group("500-2000", RangeCondition(measure, 500, 2000)),
            Group("2000-5000", RangeCondition(measure, 2000, 5000)),
            Group("5000-999999", RangeCondition(measure, 5000, 99999))
        ]

    def getTestCodeLinesChanged(self):
        measure = TestCodeLinesChanged()
        return [
            Group("0", RangeCondition(measure, 0, 1)),
            Group("0-10", RangeCondition(measure, 1, 10)),
            Group("10-30", RangeCondition(measure, 10, 30)),
            Group("30-50", RangeCondition(measure, 30, 50)),
            Group("50-100", RangeCondition(measure, 50, 100)),
            Group("100-200", RangeCondition(measure, 100, 200)),
            Group("200-500", RangeCondition(measure, 200, 500)),
            Group("500-2000", RangeCondition(measure, 500, 2000)),
            Group("2000-5000", RangeCondition(measure, 2000, 5000)),
            Group("5000-999999", RangeCondition(measure, 5000, 99999))
        ]