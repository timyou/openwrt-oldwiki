
设置数据库为紧急模式
         停掉SQL Server服务；

         把应用数据库的数据文件XXX_Data.mdf移走；

         重新建立一个同名的数据库XXX；

         停掉SQL服务；

         把原来的数据文件再覆盖回来；

         运行以下语句，把该数据库设置为紧急模式；

    运行“Use Master

Go

sp_configure 'allow updates', 1

reconfigure with override

Go”

执行结果：

DBCC 执行完毕。如果 DBCC 输出了错误信息，请与系统管理员联系。

已将配置选项 'allow updates' 从 0 改为 1。请运行 RECONFIGURE 语句以安装[http://www.raidsos.org 数据恢复]。



接着运行“update sysdatabases set status = 32768 where name = 'XXX'”

执行结果：

（所影响的行数为 1 行）



         重启SQL Server服务；

         运行以下语句，把应用数据库设置为Single User模式；

      运行“sp_dboption 'XXX', 'single user', 'true'”

执行结果：

      命令已成功完成。



         做DBCC CHECKDB；

      运行“DBCC CHECKDB('XXX')”

执行结果：

'XXX' 的 DBCC 结果。

'sysobjects' 的 DBCC 结果。

对象 'sysobjects' 有 273 行，这些行位于 5 页中。

'sysindexes' 的 DBCC 结果。

对象 'sysindexes' 有 202 行，这些行位于 7 页中。

'syscolumns' 的 DBCC 结果。

………



         运行以下语句把系统表的修改选项关掉；

      运行“sp_resetstatus "XXX"

go

sp_configure 'allow updates', 0

reconfigure with override

Go”

执行结果：

在 sysdatabases 中更新数据库 'XXX' 的条目之前，模式 = 0，状态 = 28（状态 suspect_bit = 0），

没有更新 sysdatabases 中的任何行，因为已正确地重置了模式和状态。没有错误，未进行任何更改。

DBCC 执行完毕。如果 DBCC 输出了错误信息，请与系统管理员联系。

已将配置选项 'allow updates' 从 1 改为 0。请运行 RECONFIGURE 语句以安装[http://www.fixdisk.net 数据恢复]。



         重新建立另外一个数据库XXX.Lost；

DTS导出向导
         运行DTS导出向导；

         复制源选择EmergencyMode的数据库XXX，导入到XXX.Lost；

         选择“在SQL Server数据库之间复制对象和数据”，试了多次，好像不行，只是复制过来了所有表结构，但是没有数据，也没有视图和存储过程，而且DTS向导最后报告复制失败；

         所以最后选择“从源数据库复制表和视图”，但是后来发现，这样总是只能复制一部分表记录；

         于是选择“用一条查询指定要传输的数据”，缺哪个表记录，就导哪个；

         视图和存储过程是执行SQL语句添加的。



   这样，XXX.Lost数据库就可以替换原来的应用数据库了。
[http://www.raidsos.org/cq 重庆数据恢复] 
[http://www.raidsos.org/cd/ 成都数据恢复] 
[http://www.raidsos.org/sh/ 上海数据恢复] 
[http://www.raidsos.org/sz 深圳数据恢复] 
[http://www.raidsos.org/bj/ 北京数据恢复] 
[http://www.raidsos.org/Xa/ 西安数据恢复] 
[http://www.raid120.com/ 数据恢复] 
[http://www.raid-recovery.org/ Raid数据恢复] 
[http://www.fixdisk.net/ 数据恢复] 
[http://www.raidsos.org/ypsjhf/171207776.html 硬盘数据恢复] 
[http://www.raidsos.org/ 硬盘数据恢复] 
[http://www.raid-recovery.org/ 数据恢复] 
[http://www.raid120.net/ 服务器数据恢复] 
 [http://www.datahf.net/ 数据恢复]  
[http://www.raid120.net/DiskDataFix/ 硬盘数据恢复] 
[http://www.fixdisk.net/cq 重庆数据恢复] 
[http://www.fixdisk.net/cd 成都数据恢复] 
[http://www.fixdisk.net/sh 上海数据恢复] 
[http://www.fixdisk.net/sz/ 深圳数据恢复]  
[http://www.fixdisk.net/bj/ 北京数据恢复] 
[http://www.fixdisk.net/xa/ 西安数据恢复] 
[http://www.raid120.org 服务器数据恢复]
