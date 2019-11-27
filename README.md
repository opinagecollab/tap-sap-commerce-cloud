## tap-occ-products

This is a [Singer](https://singer.io) tap that produces JSON-formatted data
following the [Singer
spec](https://github.com/singer-io/getting-started/blob/master/SPEC.md).

This tap:

- Pulls raw data from any OCC instance.
- Extracts the following product resources [ detailed data model [below](#product-data-model) ]:
  - descriptions
  - prices
  - stock status
  - categories
  - classifications
  - features
- Outputs the schema for each resource
- Incrementally pulls data based on the input state

<br>

### Tap configuration

The tap uses the following configuration object:
 
```json
{
  "scheme": "https",
  "base_url": "localhost:9002",
  "base_path": "/rest/v2",
  "base_site": "/electronics"
}
```

Sample configuration is currently stored in the `./sample_config.json` file.

<br>

### Running the tap

1. Create a virtual environment to avoid dependecy related issues
    ```text
    $ python -m venv path/to/your/venv
    ```

2. Activate your virtual environment
     ```text
    $ source path/to/your/venv/bin/activate
    ```

3. Install the tap locally
    ```text
    $ pip install -e . 
    ```
   
4. Run tap in discovery mode
    ```text
    $ tap-occ-products -c sample_config.json --discover
    ```
   
5. For more information read [this](https://github.com/singer-io/getting-started). 

<br>

### Product data model 

The resources extracted from the configured OCC instance will be stored in the data warehouse according to the following relational data model:

![warehouse schema](./doc/warehouse-schema.png)

** edit data model [here](https://www.lucidchart.com/invitations/accept/1cccf1ee-a990-49bc-a2e2-9d5fe31009ec)

---

Copyright &copy; 2019 SAP
