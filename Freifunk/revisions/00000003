= Freifunk on OpenWRT Kamikaze =
This wikipage is intended as a starting point for discussions about the requirements, architecture and implementation guidelines for OpenWRT Kamikaze Freifunk addons and/or the new Lua-Webinterface in general.

== Preliminary Thoughts ==
 * The Freifunk addon for Kamikaze will be primarily a different or modified web interface since most of the required core functionality is already provided by OpenWRT
 * The web interface will consist of a public part, visible for everyone and an adminstrative part only accesible after a successful authentication
 * The language for implementing required CGI scripts is Lua
 * CGI scripts should access the central configuration through the uci command or libuci
 * CGI scripts should generate all output through a template framework, preferably with i18n capabilities
 * CGI scripts should not access the system directly, but using a kind of abstraction layer for determining system-specific settings, devices, environment variables etc.
 * Generated HTML should conform to XHTML 1.0 strict, if applicable
 * No core functionality should solely depend on Java-Script
== Suggestions for Architecture ==
The framework for writing a Freifunk webinterface will be roughly divided in three parts:

 * A library for accessing the central configuration through uci
 * A template framework for generating html code and doing automatic translation
 * An abstraction layer to access system specific data
Some candidates for the templating toolkit and form-processing capabilities etc. are [http://haserl.sourceforge.net/ Haserl] (GPL v2) or [http://www.keplerproject.org/cgilua/ CGILua] (BSD-like license)
