This patch adds wildcard for source statements in *.in files used by {{{config}}}.
{{{
diff -Nur config.orig/lex.zconf.c_shipped config/lex.zconf.c_shipped
--- config.orig/lex.zconf.c_shipped	2005-07-10 13:43:30.000000000 -0400
+++ config/lex.zconf.c_shipped	2005-07-10 13:43:36.000000000 -0400
@@ -20,6 +20,7 @@
 #include <string.h>
 #include <errno.h>
 #include <stdlib.h>
+#include <glob.h>
 
 /* end standard C headers. */
 
@@ -3622,32 +3623,52 @@
 
 void zconf_nextfile(const char *name)
 {
-	struct file *file = file_lookup(name);
-	struct buffer *buf = malloc(sizeof(*buf));
-	memset(buf, 0, sizeof(*buf));
-
-	current_buf->state = YY_CURRENT_BUFFER;
-	zconfin = zconf_fopen(name);
-	if (!zconfin) {
-		printf("%s:%d: can't open file \"%s\"\n", zconf_curname(), zconf_lineno(), name);
+	size_t i;
+	int retval;
+	glob_t files;
+	char *filename;
+	struct file *file;
+	struct buffer *buf;
+
+	retval = glob(name, GLOB_ERR | GLOB_MARK, NULL, &files);
+	if (retval == GLOB_NOSPACE || retval == GLOB_ABORTED || retval == GLOB_NOMATCH) {
+		printf("%s:%d: glob failed: %s \"%s\"\n", zconf_curname(), zconf_lineno(),
+			retval == GLOB_NOSPACE ? "failed to allocate memory" :
+				retval == GLOB_ABORTED ? "read error" : "no match",
+			name);
 		exit(1);
 	}
-	zconf_switch_to_buffer(zconf_create_buffer(zconfin,YY_BUF_SIZE));
-	buf->parent = current_buf;
-	current_buf = buf;
 
-	if (file->flags & FILE_BUSY) {
-		printf("recursive scan (%s)?\n", name);
-		exit(1);
-	}
-	if (file->flags & FILE_SCANNED) {
-		printf("file %s already scanned?\n", name);
-		exit(1);
+	for (i = files.gl_pathc-1; i != (size_t)-1; --i) {
+		filename = files.gl_pathv[i];
+
+		file = file_lookup(filename);
+                buf = malloc(sizeof(*buf));
+		memset(buf, 0, sizeof(*buf));
+		current_buf->state = YY_CURRENT_BUFFER;
+		zconfin = zconf_fopen(filename);
+		if (!zconfin) {
+			printf("%s:%d: can't open file \"%s\"\n",
+				zconf_curname(), zconf_lineno(), filename);
+			exit(1);
+		}
+		zconf_switch_to_buffer(zconf_create_buffer(zconfin,YY_BUF_SIZE));
+		buf->parent = current_buf;
+		current_buf = buf;
+
+		if (file->flags & FILE_BUSY) {
+			printf("recursive scan (%s)?\n", filename);
+			exit(1);
+		}
+		if (file->flags & FILE_SCANNED) {
+			printf("file %s already scanned?\n", filename);
+			exit(1);
+		}
+		file->flags |= FILE_BUSY;
+		file->lineno = 1;
+		file->parent = current_file;
+		current_file = file;
 	}
-	file->flags |= FILE_BUSY;
-	file->lineno = 1;
-	file->parent = current_file;
-	current_file = file;
 }
 
 static struct buffer *zconf_endfile(void)
diff -Nur config.orig/zconf.l config/zconf.l
--- config.orig/zconf.l	2005-07-10 13:43:30.000000000 -0400
+++ config/zconf.l	2005-07-10 13:43:36.000000000 -0400
@@ -12,6 +12,7 @@
 #include <stdlib.h>
 #include <string.h>
 #include <unistd.h>
+#include <glob.h>
 
 #define LKC_DIRECT_LINK
 #include "lkc.h"
@@ -301,32 +302,52 @@
 
 void zconf_nextfile(const char *name)
 {
-	struct file *file = file_lookup(name);
-	struct buffer *buf = malloc(sizeof(*buf));
-	memset(buf, 0, sizeof(*buf));
-
-	current_buf->state = YY_CURRENT_BUFFER;
-	yyin = zconf_fopen(name);
-	if (!yyin) {
-		printf("%s:%d: can't open file \"%s\"\n", zconf_curname(), zconf_lineno(), name);
+	size_t i;
+	int retval;
+	glob_t files;
+	char *filename;
+	struct file *file;
+	struct buffer *buf;
+
+	retval = glob(name, GLOB_ERR | GLOB_MARK, NULL, &files);
+	if (retval == GLOB_NOSPACE || retval == GLOB_ABORTED || retval == GLOB_NOMATCH) {
+		printf("%s:%d: glob failed: %s \"%s\"\n", zconf_curname(), zconf_lineno(),
+			retval == GLOB_NOSPACE ? "failed to allocate memory" :
+				retval == GLOB_ABORTED ? "read error" : "no match",
+			name);
 		exit(1);
 	}
-	yy_switch_to_buffer(yy_create_buffer(yyin, YY_BUF_SIZE));
-	buf->parent = current_buf;
-	current_buf = buf;
 
-	if (file->flags & FILE_BUSY) {
-		printf("recursive scan (%s)?\n", name);
-		exit(1);
-	}
-	if (file->flags & FILE_SCANNED) {
-		printf("file %s already scanned?\n", name);
-		exit(1);
+	for (i = files.gl_pathc-1; i != (size_t)-1; --i) {
+		filename = files.gl_pathv[i];
+
+		file = file_lookup(filename);
+		buf = malloc(sizeof(*buf));
+		memset(buf, 0, sizeof(*buf));
+		current_buf->state = YY_CURRENT_BUFFER;
+		zconfin = zconf_fopen(filename);
+		if (!zconfin) {
+			printf("%s:%d: can't open file \"%s\"\n",
+				zconf_curname(), zconf_lineno(), filename);
+			exit(1);
+		}
+		zconf_switch_to_buffer(zconf_create_buffer(zconfin,YY_BUF_SIZE));
+		buf->parent = current_buf;
+		current_buf = buf;
+
+		if (file->flags & FILE_BUSY) {
+			printf("recursive scan (%s)?\n", filename);
+			exit(1);
+		}
+		if (file->flags & FILE_SCANNED) {
+			printf("file %s already scanned?\n", filename);
+			exit(1);
+		}
+		file->flags |= FILE_BUSY;
+		file->lineno = 1;
+		file->parent = current_file;
+		current_file = file;
 	}
-	file->flags |= FILE_BUSY;
-	file->lineno = 1;
-	file->parent = current_file;
-	current_file = file;
 }
 
 static struct buffer *zconf_endfile(void)
}}}
