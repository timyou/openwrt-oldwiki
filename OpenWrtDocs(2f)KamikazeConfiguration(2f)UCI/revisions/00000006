#pragma section-numbers off
||<tablebgcolor="#f1f1ed" tablewidth="40%" tablestyle="margin: 0pt 0pt 1em 1em; float: right; font-size: 0.9em;"style="padding: 0.5em;">[[TableOfContents]]||
= What is UCI =
'''U'''nified '''C'''onfiguration '''I'''nterface.

UCI is a very flexible and modular interface to store configurations in plain text files. UCI is the successor/replacement for depricated NVRAM. The text files are stored by default in /etc/config/<config> and they all have the structure like <config>.<section>.<option>=<value>. UCI was specially written for embedded systems where it makes no sense or where you have limited ressources to run a database to store the configuration. UCI is written in C and and a command-line interface is available to modify the configuration files via the shell without the need of using a text editor. The LuCI WebUI makes heavy use of UCI as well.

UCI is maintained by nbd at [http://nbd.name/gitweb.cgi?p=uci.git;a=summary UCI Library and utility for the Unified Configuration Interface for OpenWrt]

= The UCI CLI =
{{{
root@OpenWrt:~# uci
Usage: uci [<options>] <command> [<arguments>]
Commands:
        batch
        export     [<config>]
        import     [<config>]
        changes    [<config>]
        commit     [<config>]
        add        <config> <section-type>
        add_list   <config>.<section>.<option>=<string>
        show       [<config>[.<section>[.<option>]]]
        get        <config>.<section>[.<option>]
        set        <config>.<section>[.<option>]=<value>
        delete     <config>[.<section[.<option>]]
        rename     <config>.<section>[.<option>]=<name>
        revert     <config>[.<section>[.<option>]]
Options:
        -c <path>  set the search path for config files (default: /etc/config)
        -d <str>   set the delimiter for list values in uci show
        -f <file>  use <file> as input instead of stdin
        -m         when importing, merge data into an existing package
        -n         name unnamed sections on export (default)
        -N         don't name unnamed sections
        -p <path>  add a search path for config change files
        -P <path>  add a search path for config change files and use as default
        -q         quiet mode (don't print error messages)
        -s         force strict mode (stop on parser errors, default)
        -S         disable strict mode
}}}
