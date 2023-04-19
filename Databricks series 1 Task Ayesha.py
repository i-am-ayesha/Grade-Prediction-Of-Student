# Databricks notebook source
df= spark.range(1000)

# COMMAND ----------

df.show()

# COMMAND ----------

df.createOrReplaceTempView("Test")

# COMMAND ----------

# MAGIC %sql
# MAGIC select * from Test;

# COMMAND ----------

# MAGIC %run /Users/odl_user_919118@databrickslabs.com/data-engineering-with-databricks/Includes/Classroom-Setup-01.2 

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT * FROM demo_tmp_vw

# COMMAND ----------

print(f"DA:                   {DA}")
print(f"DA.username:          {DA.username}")
print(f"DA.paths.working_dir: {DA.paths.working_dir}")
print(f"DA.schema_name:       {DA.schema_name}")

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT '${da.username}' AS current_username,
# MAGIC        '${da.paths.working_dir}' AS working_directory,
# MAGIC        '${da.schema_name}' as schema_name

# COMMAND ----------

path = f"{DA.paths.datasets}"
dbutils.fs.ls(path)

# COMMAND ----------

path = f"{DA.paths.datasets}"
files = dbutils.fs.ls(path)
display(files)

# COMMAND ----------

dbutils.fs.help()

# COMMAND ----------

dbutils.fs.mount?

# COMMAND ----------

dbutils.widgets.help()

# COMMAND ----------

dbutils.widgets.text("Name","Ayesha")

# COMMAND ----------

dbutils.widgets.get("Name")

# COMMAND ----------

dbutils.widgets.dropdown("Color","Blue",["Red","Blue","Black"])

# COMMAND ----------

dbutils.widgets.get("Color")

# COMMAND ----------


