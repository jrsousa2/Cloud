# When working with a cluster of machines, the machine that submits
# the codes is the driver machine (or worker/master)
# The master is the orchestrator that splits the workload among the workers
# The cluster manager manages the tasks based on the user requests (driver machine)
and puts all the results together at the end of the process.
# Azure Data Lake emulates HDFS (Hadoop) but is implemented much more efficiently

# The Spark engine has support for Python, R, Scala (native), Java and SQL
Spark is what speeds up the processing, it runs multiple processes concurrently
in parallel 
It's interesting to note that files created by Spark on multiple machines run in on parallel on will be separate if say they get saved to blob storage.
This exemplifies the core principle of what parallel processig means.

# Databricks uses the same notebook format as Jupyter like a cmd prompt
In AWS or Azure Databricks automatically attaches itelf to the S3 or Blob storage

One interesting feature of the Databricks managmt console or UI is the ability to attach machine clusters, pause them and restart them as needed
Databricks manages the cluster creation so the user doesn't have to do that in Spark

With Databricks you can also schedule jobs.

Permission settings are all over the place to choose who can view/run my notebooks,
share the cluster, create clusters, etc.
Databricks Permissions are integrated with Active Directory in Azure (the main platform
for Databricks).

Dbutils allows the user to attach an external storage such as Azure blob storage
or AWS S3 bucket. It allows it to be used like it was local storage, and it's also
the storage device used by the Spark engine as it runs.

Databricks adds enhancement which improve the performance of pure Spark.

The API for databricks was designed for the cloud.

Databricks adds on top of Spark engine: machine Clusters mgmt, Folders, Libraries,
Notebooks, Security and Job scheduling.

Databricks also allows Python libraries to be added for more functionality.

# Create a large list of numbers
nums = list(range(0,1000001))

# Spark distributes the data across multiple machines or cluster

# Parallelize (take a python list and distribute into an rdd - resilient distributed dataset)
# sc is short for SparkContext

# The below syntax won't work with a serverless Notebook in Databricks
# Needs to create and attach a cluster for this to work
nums_rdd = sc.parallelize(nums)

# Using lambda functions with the list
rdd = sc.parallelize([1, 2, 3, 4])
rdd_squared = rdd.map(lambda x: x * x)
print(rdd_squared.collect())  # Output: [2, 4, 6, 8]


# Shows a subset of the RDD list
nums_rdd.take(5)

# Another example, with a tuple

pairs = rdd_squared.map(lambda x: (x, len(str(x))))

# Shows pairs
pairs.take(5)

# Filter certain elements from the list 
# Selects pairs where the number of digits of the first element is even
even_dig_pairs = pairs.filter(lambda x: x[1] % 2==0)

# Flip the created pairs
flip_pairs = pairs.map(lambda x: (x[1], x[0]))
