# HOW-TO: Starting a New Project

## Table of Contents

- [Prequisites](#prerequisites)
- [Step-1: Create a new repository](#step-2-create-a-new-repository)
- [Step-2: Add the source text](#step-1-add-the-source-text)
- [Step-3: Configure the languages](#step-2-configure-the-languages)
- [Step-4: Create the translation resources](#step-3-create-the-translation-resources)
- [Step-5: Create a new project in Transifex](#step-4-create-a-new-project-in-transifex)
- [Step-6: Making the connection between Github and Transifex](#step-5-making-the-connection-between-github-and-transifex)
- [Step-7: Starting working in Transifex](#step-6-starting-working-in-transifex)

## Prerequisites 

### On Github

- [ ] You have a Github account
- [ ] You have created a Github organization (this is where all your projects will live)
- [ ] You have been added to the [BuddhistCAT](https://github.com/BuddhistCAT/) Github organization

### On Transifex

- [ ] You have connected Transifex with your Github Organization (see how here: https://www.youtube.com/watch?v=cdhndeB-1N0&t=0s)


## Step-1: Create a new repository

For every project, or however you want to break things down (texts, chapters, etc.), there will be a Github repository.

<img width="1330" alt="Screenshot 2023-01-13 at 13 08 36" src="https://user-images.githubusercontent.com/7943188/212306289-c91969c4-430a-4a16-bad9-4b3fc1b2c8db.png">

Once you have clicked `new repository` from the menu, the dialogue for creating a new repository will be opened. The key point here is to select the `BuddhistCAT/New-Project-Template`:

<img width="1330" alt="Screenshot 2023-01-13 at 13 10 16" src="https://user-images.githubusercontent.com/7943188/212306652-b5d6c7b3-bd2c-4131-9f25-8ec1c38a42cf.png">

For the rest, make sure that the `Owner` field is set to the organization where you want to keep your projects on Github.

## Step-2: Add the source text

Start by adding the source text to [root/001.txt](../root/001.txt) file. 

**NOTE:** The source text should be segmented in the way where each line in the file represents a fragment of text to be translated (i.e. loosely speaking a sentence).

## Step-2: Configure the languages

If you are translating to other language than English, set the `SOURCE_LANGUAGE` and `TARGET_LANGUAGE` variables in [.languages](../.languages). 

**NOTE:** The language codes have to be in the same form as in Transifex. Defaults are `bo` (Tibetan) for `SOURCE_LANGUAGE` and `en` (English) for `TARGET_LANGUAGE`.

## Step-3: Create the translation resources 

Create a new branch in Github named `first_phase` by clicking the branches selector, then typing `first_phase` into the text and clicking `Create branch`. This will automatically prepare everything for Transifex. 

NOTE: The status of the automated process can be followed in `Actions` tab.

Once the automated process has completed, go to `Pull Requests` tab and create a new pull request where the base is `main` and compare is `first_phase` and click `Create pull request`.

## Step-4: Create a new project in Transifex

Go to `Dashboard` from the top navigation menu and click `Create new project` button from the bottom of the screen.

Give a name to your project, and choose `File based: Upload a language file (eg. po, yml, xliff) with your contents` under the `Choose project type` heading. Set `Source language` and `Target language` and then click `Create project`. 

**NOTE:** The language settings here have to correspond with the language settings from [Step-2: Configure the languages](#step-2-configure-the-languages). The default is `bo` and `en`. 

Once project is created, after clicking `Settings` below the name of the project on the left navigation pane, go to the bottom of the `General` settings and check `My project is a non-commercial Open Source project` and paste the URL of the Github repository for your project in the opening text field. Click `Save changes`.

**NOTE:** If your project is not available in [Creative Commons](https://creativecommons.org/) or other permissive open source license, you have to pay for Transifex.

## Step-5: Making the connection between Github and Transifex

Start by clicking the project name on the left navigation pane, and then choosing `Settings`.

From `Settings` choose `Integrations` tab and under the section `Github` click `Link Repository`. Select the repository you want to connect from the dropdown menu under `Transifex will pull content from this repository.`. Then select `main` from the drop down under `
The integration will work with this branch only.` Click `Next`.

Make sure that under `Add a path to your YAML config file` it says `transifex.yml` and click `Apply`. 

Set `Push translations` to `100% translated or updated (for 100% translated) and under `How would you like Transifex to push translations to GitHub?` choose `Commit directly`. Then click `Save & Sync`. 

## Step-6: Starting working in Transifex

You are now all set and ready to translate. Have fun!
