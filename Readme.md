# Translation parser Python

## Important

- The library is using Python3, run `python3 -m pip install -r requirements.txt`
- The library by default export only `en-US` language, you can extend it by changing the variable `language` in `common.py` file

## Convert JSON to Xlsx to export at business

- Copy your plain `translation.json` here `./inputs/translation.json`
- **IMPORTANT** if you have these keys: `en-US`(depending on the language), or `translation` wrapping the plain translations in your json file **Remove them** you need the plain translations in your input file
- Launch the command `python3 translation-json-to-xlsx.py`
- The output file is in this path `./outputs/exported-xlsx/translation-{Timestamp}.xlsx`

## Convert JSON Multilanguage to Xlsx to export at business

- Copy your plain `translation.json` here `./inputs-multiple/[region(ex: en-US)]/translation.json`
- **Important** all the translation files **MUST** have the exact keys for each language
- Launch the command `python3 translation-json-to-xlsx-multiple.py`
- The output file is in this path `./outputs/exported-xlsx-multiple/translation-{Timestamp}.xlsx`

## Convert Xlsx to merged JSON to import the newest labels (merging with the actual)

- Copy your plain `translation.json` here `./inputs/translation.json`
- **IMPORTANT** if you have these keys: `en-US`(depending on the language), or `translation` wrapping the plain translations in your json file **Remove them** you need the plain translations in your input file
- Copy your plain `translation.xlsx` here `./inputs/translation.xlsx`
- Launch the command `python3 xlsx-to-json-merged`
- The output file is in this path `./outputs/merged-translations/translation-{Timestamp}.json`

## Convert Xlsx to merged JSON Multilanguage to import the newest labels (merging with the actual)

- Copy your plain `translation.json` here `./inputs-multiple/[region(ex: en-US)]/translation.json`
- Copy your plain `translation.xlsx` here `./inputs/translation.xlsx`
- The xlsx table must be structured like this:

```markdown
| Translation ID | language-1     | language-2     | language-...     |
| -------------- | -------------- | -------------- | ---------------- |
| translation.id | value-in-lng-1 | value-in-lng-2 | value-in-lng-... |
```

- Launch the command `python3 xlsx-to-json-merged-multiple`
- The output file is in this path `./outputs/merged-translations-multiple/{Timestamp}/[region(ex: en-US)]/translation.json`
