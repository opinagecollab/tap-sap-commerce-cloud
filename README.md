## tap-occ-products

This is a [Singer](https://singer.io) tap that produces JSON-formatted data
following the [Singer
spec](https://github.com/singer-io/getting-started/blob/master/SPEC.md).

This tap:

- Pulls raw data from any __SAP Commerce Cloud__ instance
- Extracts the following product resources:
  - categories
  - product details
  - product specifications
- Outputs the schema for each resource

Copyright &copy; 2020 SAP
