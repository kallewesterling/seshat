Setting up Seshat
=================

This page instructs software engineers how to get started working with the Django codebase and PostgreSQL database for the "core" Seshat webapp. It assumes the engineer has access to a dumpfile of the Seshat "core" database.


Setting up in the cloud
-----------------------

We use Pulumi to manage our cloud infrastructure. To set up the infrastructure, you will need to install Pulumi and configure your Azure credentials.

Instructions for installing Pulumi can be found :doc:`here </getting-started/setup/cloud/pulumi>`.


Setting up in a local environment
---------------------------------

We also have instructions for how to set up Seshat in a local environment. You can find these instructions :doc:`here </getting-started/setup/local/index>`.


.. toctree::
   :maxdepth: 1

   cloud/pulumi
   local/index
   spatialdb