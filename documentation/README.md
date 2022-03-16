### Prequisites 

- You have created a new repository which has the contents of [Transifex Workflow Template](https://github.com/Lotus-King-Translation/Transifex-Backend-Template)
- You have created a [Personal Github Access Token](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token)
- You have added the `Personal Access Token` as a [secret into the new repository](https://docs.github.com/en/codespaces/managing-codespaces-for-your-organization/managing-encrypted-secrets-for-your-repository-and-organization-for-codespaces#adding-secrets-for-a-repository) with name `GIT_TOKEN`

### 1) Add the source text

Start by adding the source text to [root/001.txt](../root/001.txt) file. 

**NOTE:** The source text should be segmented in the way where each line in the file represents a fragment of text to be translated (i.e. loosely speaking a sentence).

### 2) Create the translation resources 

Create a new branch in Github named `first_phase` by clicking the branches selector, then typing `first_phase` into the text and clicking `Create branch`. This will automatically prepare everything for Transifex. 

NOTE: The status of the automated process can be followed in `Actions` tab.

Once the automated process has completed, go to `Pull Requests` tab and create a new pull request where the base is `main` and compare is `first_phase` and click `Create pull request`.

### 3) Create a new project in Transifex

Go to `Dashboard` from the top navigation menu and click `Create new project` button from the bottom of the screen.

Give a name to your project, and choose `File based: Upload a language file (eg. po, yml, xliff) with your contents` under the `Choose project type` heading. Set `Source language` and `Target language` and then click `Create project`. 

**NOTE:** The directory names in [wip/](../wip) directory have to correspond with the source and target language codes in Transifex. The default is `bo` and `en`. 

Once project is created, after clicking `Settings` below the name of the project on the left navigation pane, go to the bottom of the `General` settings and check `My project is a non-commercial Open Source project` and paste the URL of the Github repository for your project in the opening text field. Click `Save changes`.

**NOTE:** If your project is not available in [Creative Commons](https://creativecommons.org/) or other permissive open source license, you have to pay for Transifex.

### 4) Making the connection between Github and Transifex

Start by clicking the project name on the left navigation pane, and then choosing `Settings`.

From `Settings` choose `Integrations` tab and under the section `Github` click `Link Repository`. Select the repository you want to connect from the dropdown menu under `Transifex will pull content from this repository.`. Then select `main` from the drop down under `
The integration will work with this branch only.` Click `Next`.

Make sure that under `Add a path to your YAML config file` it says `transifex.yml` and click `Apply`. 

Set `Push translations` to `100% translated or updated (for 100% translated) and under `How would you like Transifex to push translations to GitHub?` choose `Commit directly`. Then click `Save & Sync`. 
