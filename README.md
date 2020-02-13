# compare.py

## Requirements:
* Python 3.x (Replace `python` in below commands with `python3` if you have Python 2.x installed as `python` and Python 3.x as `python3`)

## Usage:

```
python compare.py <file_1> <file_2>
```

## Example:

```
python compare.py fixtures/file_1 fixtures/file_2
```

## Assumptions:

1. If there more lines in file_1 than file_2, then lines not present in file_2 are skipped.
2. If there more lines in file_2 than file_1, then lines not present in file_1 are skipped.
3. If a line is empty in either file_1 or file_2, that line is skipped.
4. If the URL is invalid in file_1 or file_2, that line is skipped. The request error is stored in "errors.log" file with line number.
5. If the response code is non-2xx, that line is skipped. The response error is stored in "errors.log" file with line number.
6. If the response body is not JSON, that line is skipped. The parsing error is stored in "errors.log" file with line number.

## Random Link Generation:

* Use fixtures/gen.py to generate test data.
* Modify `number_of_lines` / URLs in the file to increase number of lines and/or modify URLs.

## Tests

* Run `python compare_test.py`
