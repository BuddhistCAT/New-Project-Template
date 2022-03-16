### 1) Add the source text

Start by adding the source text to [root/001.txt](../root/001.txt) file. 

**NOTE:** The source text should be segmented in the way where each line in the file represents a fragment of text to be translated (i.e. loosely speaking a sentence).

### 2) Create the translation resources 

Create a new branch in Github named `first_phase` by clicking the branches selector, then typing `first_phase` into the text and clicking `Create branch`. This will automatically prepare everything for Transifex

### 3) Create a new project in Transifex

Go to `Dashboard` from the top navigation menu and click `Create new project` button from the bottom of the screen.

Give a name to your project, and choose `File based: Upload a language file (eg. po, yml, xliff) with your contents` under the `Choose project type` heading. Set `Source language` and `Target language` and then click `Create project`. 

**NOTE:** The directory names in [wip/](../wip) directory have to correspond with the source and target language codes in Transifex. The default is `bo` and `en`. 

### 4) Making the connection between Github and Transifex

Start by clicking the project name on the left navigation pane, and then choosing `Settings`.

From `Settings` choose `Integrations` tab.

```
filters:
  - filter_type: file
    file_format: PO
    source_language: bo
    source_file: wip/bo/001.po
    translation_files_expression: 'wip/<lang>/001.po'
```

NOTE: The `source_language` field and `source_file` both have to correspond with the source language of the project. The above example is for `bo` (Tibetan). In the case of the source language being English, the following will work: 

```
filters:
  - filter_type: file
    file_format: PO
    source_language: en
    source_file: wip/en/001.po
    translation_files_expression: 'wip/<lang>/001.po'
```
