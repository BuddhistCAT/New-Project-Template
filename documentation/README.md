## Table of Contents

- [Prequisites](#prerequisites)
- [Step-1: Add the source text](#step-1-add-the-source-text)
- [Step-2: Configure the languages](#step-2-configure-the-languages)
- [Step-3: Create the translation resources](#step-3-create-the-translation-resources)
- [Step-4: Create a new project in Transifex](#step-4-create-a-new-project-in-transifex)
- [Step-5: Making the connection between Github and Transifex](#step-5-making-the-connection-between-github-and-transifex)
- [Step-6: Starting working in Transifex](#step-6-starting-working-in-transifex)

## Prerequisites 

- You have created a repository by forking [Transifex Workflow Template](https://github.com/Lotus-King-Translation/Transifex-Backend-Template) following the instructions [found here](https://docs.github.com/en/get-started/quickstart/fork-a-repo#forking-a-repository)
- You have created a [Personal Github Access Token](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token)
- You have added the `Personal Access Token` as a [secret into the new repository](https://docs.github.com/en/codespaces/managing-codespaces-for-your-organization/managing-encrypted-secrets-for-your-repository-and-organization-for-codespaces#adding-secrets-for-a-repository) with name `GIT_TOKEN`

## Step-1: Add the source text

Start by adding the source text to [root/001.txt](../root/001.txt) file. 

**NOTE:** The source text should be segmented in the way where each line in the file represents a fragment of text to be translated (i.e. loosely speaking a sentence).

## Step-2: Configure the languages

Set the `SOURCE_LANGUAGE` and `TARGET_LANGUAGE` variables in [.languages](../.languages). 

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
