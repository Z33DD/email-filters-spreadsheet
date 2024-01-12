<p align="center">
  <img src="https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-markdown-open.svg" width="100" />
</p>
<p align="center">
    <h1 align="center">EMAIL-FILTERS-SPREADSHEET</h1>
</p>
<p align="center">
    <em>Sift, Sort, Simplify: Email Filtering Made Easy</em>
</p>
<p align="center">
	<img src="https://img.shields.io/github/license/Z33DD/email-filters-spreadsheet" alt="license">
	<img src="https://img.shields.io/github/last-commit/Z33DD/email-filters-spreadsheet?style=default&color=0080ff" alt="last-commit">
	<img src="https://img.shields.io/github/languages/top/Z33DD/email-filters-spreadsheet?style=default&color=0080ff" alt="repo-top-language">
	<img src="https://img.shields.io/github/languages/count/Z33DD/email-filters-spreadsheet?style=default&color=0080ff" alt="repo-language-count">
<p>
<p align="center">
	<!-- default option, no dependency badges. -->
</p>


##  Overview

The email-filters-spreadsheet a script to generate [Sieve filters](https://en.wikipedia.org/wiki/Sieve_(mail_filtering_language)) from a Google Sheets spreadsheet.
It was created because ProtonMail has a very bad filter management UX.


##  Repository Structure

```sh
└── email-filters-spreadsheet/
    ├── life_script
    │   └── sheets.py
    ├── pyproject.toml
    └── templates
        ├── filter_template.siv
        └── header.siv
```


##  Getting Started

***Requirements***

Ensure you have the following dependencies installed on your system:

* **<code>Python</code>**: `version 3.11`
* **<code>Poetry</code>**: `version 1.6.1`

###  Installation

1. Clone the email-filters-spreadsheet repository:

```sh
git clone https://github.com/Z33DD/email-filters-spreadsheet
```

2. Change to the project directory:

```sh
cd email-filters-spreadsheet
```

3. Install the dependencies:

```sh
poetry install
```

###  Running email-filters-spreadsheet

Use the following command to run email-filters-spreadsheet:

```sh
poetry run python main.py
```


##  Contributing

Contributions are welcome! Here are several ways you can contribute:

- **[Submit Pull Requests](https://github/Z33DD/email-filters-spreadsheet/blob/main/CONTRIBUTING.md)**: Review open PRs, and submit your own PRs.
- **[Join the Discussions](https://github/Z33DD/email-filters-spreadsheet/discussions)**: Share your insights, provide feedback, or ask questions.
- **[Report Issues](https://github/Z33DD/email-filters-spreadsheet/issues)**: Submit bugs found or log feature requests for Email-filters-spreadsheet.

<details closed>
    <summary>Contributing Guidelines</summary>

1. **Fork the Repository**: Start by forking the project repository to your GitHub account.
2. **Clone Locally**: Clone the forked repository to your local machine using a Git client.
   ```sh
   git clone https://github.com/Z33DD/email-filters-spreadsheet
   ```
3. **Create a New Branch**: Always work on a new branch, giving it a descriptive name.
   ```sh
   git checkout -b new-feature-x
   ```
4. **Make Your Changes**: Develop and test your changes locally.
5. **Commit Your Changes**: Commit with a clear message describing your updates.
   ```sh
   git commit -m 'Implemented new feature x.'
   ```
6. **Push to GitHub**: Push the changes to your forked repository.
   ```sh
   git push origin new-feature-x
   ```
7. **Submit a Pull Request**: Create a PR against the original project repository. Clearly describe the changes and their motivations.

Once your PR is reviewed and approved, it will be merged into the main branch.

</details>


##  License

This project is protected under [The Unlicense](https://unlicense.org). For more details, refer to the [LICENSE](LICENSE) file.
