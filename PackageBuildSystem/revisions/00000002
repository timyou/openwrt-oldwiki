= New Package Buildsystem =

== Basic Idea ==
 * package/: contains directories for each category
 * package/<category>/: contains directories for each package in this category
 * package/<category>/<package>/: all package specific information are in this directory:
   * Makefile
   * target.mk
   * Config.in
   * ipkg/<package>.control
   * patches/ (optional)

== Build Files ==
package/Makefile
{{{
# Main makefile for the packages
include $(TOPDIR)/rules.mk

include $(TOPDIR)/package/*/*/target.mk

all: compile install
clean: $(patsubst %,%-clean,$(package-) $(package-y) $(package-m))
compile: $(patsubst %,%-compile,$(package-y) $(package-m))
install: $(patsubst %,%-install,$(package-y))

%-prepare:
        @[ -f $(STAMP_DIR)/.$@ ] || $(MAKE) -C */$(patsubst %-prepare,%,$@) prepare
        @touch $(STAMP_DIR)/.$@

%-compile: %-prepare 
        @[ -f $(STAMP_DIR)/.$@ ] || $(MAKE) -C */$(patsubst %-compile,%,$@) compile
        @touch $(STAMP_DIR)/.$@

%-install: %-compile
        @[ -f $(STAMP_DIR)/.$@ ] || $(MAKE) -C */$(patsubst %-install,%,$@) install
        @touch $(STAMP_DIR)/.$@

%-rebuild: 
        @rm -f $(STAMP_DIR)/.$(patsubst %-rebuild,%,$@)-*
        $(MAKE) -C */$(patsubst %-rebuild,%,$@) rebuild

%-clean:
        @$(MAKE) -C */$(patsubst %-clean,%,$@) clean
        @rm -f $(STAMP_DIR)/.$(patsubst %-clean,%,$@)-*
}}}

package/Config.in
{{{
menu "OpenWrt Package Selection"
source "package/*/Config.in"
endmenu

source "package/Sysconf.in"
}}}

package/<category>/Config.in
{{{
menu "<category name>"
comment "<category description>"
source "package/<category>/*/Config.in"
endmenu
}}}

package/<category>/<package>/target.mk
{{{
package-$(BR2_PACKAGE_<PACKAGE>) += <package>
<package>-compile: <package-depencies>
}}}

== config Patch ==
The menuconfig configuration files (*.in) does currently not support wildcards in the source-statement. This patch is required to do this: ["PackageBuildSystemConfigPatch"].

== Package Categories ==
["PackageBuildSystemCategories"]

== TODO ==
 * Write ["PackageCreation"] for documentation on package creation.
 * Move packages/config/ out of packages/.
 * Create good categories and assign each package to one category.
 * Move bootscripts/configuration files which are specific to a package or option of a package from target/default/target_skeleton/ into the package?
 * Shall Sysconf.in stay in package directory?
 * Commit changes to cvs {{{:)}}}
