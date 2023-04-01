# Program allows to merge pdf files using Python

## How to use

### Install required packages

```sh
python -m pip install -r requirements.txt
```

### Run program

```sh
python merge_pdf.py <parameters>
```

Example

```sh
python merge_pdf.py -f path/filename1.pdf -f path/filename2.pdf --output_path path/to/output/dir --output_name output_file_name
```

### Help (available parameters)

```sh
python merge_pdf.pg --help
```

```
Usage: merge_pdf.py [OPTIONS]

Options:
  -f, --files TEXT        Insert path to pdf file to merge (use parameter
                          multiple times, once per file path)  -o, --output_path TEXT  Path where new file will be created (without file
                          name)
  -n, --output_name TEXT  Name of new file (without .pdf extesion)
  --help                  Show this message and exit.
  ```
