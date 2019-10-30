导出csv
·	格式化时间 
·	输入path和csv 判断目录和文件是否存在
·	获得tabnm 和 cond
·	获得符合条件数据量 select count(*) from tabnm where cond
·	获得列序号
·	生成printsql
·	spool on
·	运行printsql，获得结果
·	spool off

	







set pages 0
spool D:\1.Project\test\tdata.csv
select id||','||WHAT||','||status||','||MANAGER_ID||','||datetime from tdata where rownum<100;
spool off;

SELECT table_name, LISTAGG(column_name, '||'',''||') WITHIN GROUP (ORDER BY column_name) AS col
FROM   user_tab_columns where table_name='TDATA'
GROUP BY table_name;

--SELECT 'select '||to_char(wm_concat(cols))||' from '|| table_name FROM (
--SELECT '"'||column_name||'"' AS cols,table_name from user_tab_columns WHERE table_name='{0}' )
--group by table_name

SELECT table_name, LISTAGG(column_name, '||'',''||') WITHIN GROUP (ORDER BY column_id) AS col
FROM   user_tab_columns where table_name='TDATA'
GROUP BY table_name;