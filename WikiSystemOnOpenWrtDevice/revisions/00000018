= Wiki system on OpenWrt device =
Is there any wiki systems that can be [http://forum.openwrt.org/viewtopic.php?id=6324 installed on OpenWrt device]?

----
Small table pulling a few small wiki systems. There are many more though: [wiki:WikiPedia:List_of_wiki_software see this list] 
and to make detailed comparisons visit [http://www.wikimatrix.org WikiMatrix].

|| ||'''Written ''''''with''' ||'''Flat file or''' '''database''' ||'''Requirements''' (server) ||'''Requirements''' (client) ||'''GPL''' ||'''Tested?'''||'''Other info''' ||
||[http://leaf-project.org/ Leaf-project]s [http://http://leaf-project.org/devel/index.php?module=pagemaster&PAGE_user_op=view_page&PAGE_id=91&MMN_position=92:86 muwiki] (plugin) || || || ||No || || ||Uses 'WikiPedia:sed' as rendering engine. ||
||[http://www.tiddlywiki.com/ TiddlyWiki] || || || ||[wiki:WikiPedia:JavaScript Javascript] || || ||Router only saves updated contents. ||
||[http://didiwiki.org/ DidiWiki] ||C ||Flat files ||libgcc package||No ||Yes ||Works. ||Very small ~25kB and fast. See DidiWiki and BuildingPackagesHowTo for binary link. Runs only on port 8000.||
||[http://www.oddmuse.org/cgi-bin/wiki Oddmuse wiki engine] ||Perl ||Flat files ||Perl? ||No || || ||Based on UseModWiki||
||[http://pmwiki.org/ PmWiki] ||PHP ||Flat files ||PHP 4.1.x >= ||No ||Yes || ||Needs more space than OpenWrt Flash mems have. ||
||[http://www.wikini.net/wakka.php?wiki=HomePage WikiNi] || || || || || || || ||
||[http://www.usemod.com/cgi-bin/wiki.pl?UseModWiki UseModWiki]||Perl||Flat files||Perl||No|| || ||Try MicroPerl||
||[http://wikish.do.homeunix.org/ WikiSH] ||Awk ||Flat files ||None ||No || || ||Small and designed for embedded systems. Awk is part of OpenWrt. Based on [http://awkiawki.bogosoft.com AwkiAwki] ||
||[http://www.awk-scripting.de/cgi/wiki.cgi/yawk/00-WikiIndex Yark]||Gawk/C||Flat files||Gawk|| || || ||OpenWrt doesn't have Gawk but a [http://www.ipkg.be/search?q=awk Mawk] package is available which may work.||
Please update! :)

----
DidiWiki (binary file is attached to this page and an ipkg is now available) fits happily on an OpenWrt system's flash memory. 
You may need to add a symbolic link in /lib using ''ln -s /lib/libc.so.0 /lib/libgcc_s.so.1''
Start with:  
  env DIDIWIKIHOME=/opt/share/.didiwiki didiwiki
Where didiwiki is the binary file's name and .didiwiki is directory created for storing data files.
Warning: If you don't start DidiWiki with the env command your pages will be saved in the home (/tmp) directory and wil be lost on rebooting!
