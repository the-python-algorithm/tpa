# Contributing to TPA

**The Python Algorithm** uses GitHub to manage contributions. Contributions take the form of pull requests that will be reviewed by the core team.

When contributing to this repository, please first discuss the change you wish to make via issue, email, or any other method with the owners of this repository before making a change.

Please note we have a code of conduct, please follow it in all your interactions with the project.

### Table of Contents

[Code of Conduct](#code-of-conduct)

[How Can I Contribute?](#how-can-i-contribute)
  * [Reporting Bugs](#reporting-bugs)
  * [Suggesting Enhancements](#suggesting-enhancements)
  * [Your First Code Contribution](#your-first-code-contribution)
  * [Pull Requests](#pull-requests)

[Additional Notes](#additional-notes)
  * [Issue and Pull Request Labels](#issue-and-pull-request-labels)
  * [Connect with other contributors](#connect-with-other-contributors)

## Code of Conduct
This project and everyone participating in it is governed by the [TPA Code of Conduct](CODE_OF_CONDUCT.md). By participating, you are expected to uphold this code. Please report unacceptable behavior to [the-python-algorithm@outlook.com](mailto:the-python-algorithm@outlook.com).

## How Can I Contribute?
A great way to contribute to the project is to send a detailed report when you encounter an issue. We always appreciate a well-written, thorough bug report, and will thank you for it!

### Reporting Bugs
This section guides you through submitting a bug report for TPA. Following these guidelines helps maintainers and the community understand your report, reproduce the behaviour, and find related reports.

Bugs are tracked as [GitHub issues](https://guides.github.com/features/issues/).

Check that [our issue database](https://github.com/the-python-algorithm/tpa/issues) doesn't already include that problem before submitting an issue. If you find a match, you can use the "subscribe" button to get notified on updates. Do not leave random "+1" or "I have this too" comments, as they only clutter the discussion, and don't help resolving it. However, if you have ways to reproduce the issue or have additional information that may help resolving the issue, please leave a comment.

While creating an issue on this repository, provide the following information by filling in [our report bug template](https://github.com/the-python-algorithm/.github/blob/master/ISSUE_TEMPLATE/report_bug.md).
Explain the problem and include additional details to help maintainers reproduce the problem:
* **Use a clear and descriptive title** for the issue to identify the problem.
* **Describe the exact steps which reproduce the problem** in as many details as possible.
* **Provide specific examples to demonstrate the steps**. Include links to files or GitHub projects,
 or copy/pasteable snippets, which you use in those examples. If you're providing snippets in the 
 issue, use [Markdown code blocks](https://help.github.com/articles/markdown-basics/#multiple-lines).
* **Describe the behavior you observed after following the steps** and point out what exactly is the
 problem with that behavior.
* **Explain which behavior you expected to see instead and why.**
* **Include details about your configuration and environment** like name and version of OS and 
Python you are using.

### Suggesting Enhancements
This section guides you through submitting an enhancement suggestion for TPA, including completely new features and minor improvements to existing functionality. Following these guidelines helps maintainers and the community understand your suggestion and find related suggestions.

Before creating enhancement suggestions, check that [our issue database](https://github.com/the-python-algorithm/tpa/issues) doesn't already include that suggestion before submitting an issue. If you find a match, you can use the "subscribe" button to get notified on updates. Do not leave random "+1" or "I have this too" comments, as they only clutter the discussion, and don't help resolving it. However, if you have ways to reproduce the issue or have additional information that may help resolving the issue, please leave a comment. 

While creating an enhancement suggestion, fill in [our feature report template](https://github.com/the-python-algorithm/.github/blob/master/ISSUE_TEMPLATE/feature_report.md), including the steps that you imagine and provide the following information:

* **Use a clear and descriptive title** for the issue to identify the suggestion.
* **Provide a step-by-step description of the suggested enhancement** in as many details as possible.
* **Provide specific examples to demonstrate the steps**. Include copy/pasteable snippets which you 
use in those examples, as [Markdown code blocks](https://help.github.com/articles/markdown-basics/#multiple-lines).
* **Describe the current behavior** and **explain which behavior you expected to see instead** and why.
* **List some other use-cases or applications where this enhancement could be beneficial.**

### Your First Code Contribution
Unsure where to begin contributing to TPA? You can start by looking through these `good-first-issue`
 and `help-wanted` issues:

* [Good First issues][good-first-issue] - issues which should only require a few lines of code, and
 a test or two and might be helpful in understanding the particular component of the feature.
* [Help wanted issues][help-wanted] - issues which should be a bit more involved than 
`good-first-issue` issues.

Both issue lists are sorted by total number of comments. While not perfect, number of comments is a 
reasonable proxy for impact a given change will have.

### Pull Requests
The process described here has several goals:

- To maintain TPA's code quality.
- Prioritize to fix problems that are important to users.
- Engage the community in working toward the best possible issues and features.
- Enable a sustainable system for TPA's maintainers to review contributions.

Please follow these steps to have your contribution considered by the maintainers:
1. Follow all instructions in [our pull request template][tpa-pull-request-template].
2. Follow the [contributors guide][tpa-contributors-guide].
3. After you submit your pull request, verify that all [status checks](https://help.github.com/articles/about-status-checks/) are passing <details><summary>What if the status checks are failing?</summary>If a status check is failing, and you believe that the failure is unrelated to your change, please leave a comment on the pull request explaining why you believe the failure is unrelated. A maintainer will re-run the status check for you. If we conclude that the failure was a false positive, then we will open an issue to track that problem with our status check suite.</details>

While the prerequisites above must be satisfied prior to having your pull request reviewed, the reviewer(s) may ask you to complete additional design work, tests, or other changes before your pull request can be ultimately accepted.

## Additional Notes

### Issue and Pull Request Labels

This section lists the labels we use to help us track and manage issues and pull requests.

#### Type of Issue and Issue State

| Label name | Description |
| --- | --- |
| `feature` | For a new feature requests. |
| `enhancement` | The requested improvements in the existing feature. |
| `bug` | Confirmed bugs or reports that are very likely to be bugs. | 
| `question` | Questions more than bug reports or feature requests (e.g. how do I do X). |
| `duplicate` | Issues which are duplicates of other issues, i.e. they have been reported before. |
| `wontfix` | The TPA's core team has decided not to fix these issues for now, either because they're working as intended or for some other reason. |
| `invalid` | Issues which aren't valid (e.g. user errors). |
| `help-wanted` | The TPA's core team would appreciate help from the community in resolving these issues. |
| `good-first-issue` | Good for newcomers. |
| `backlog` | Issues that the TPA's core team has decided to catered after the next release. |
| `documentation` | Related to any type of documentation. |

#### Feature Specific Labels

| Label name | Description |
| --- | --- |
| `data-structure` | All the issues related to the Data structure module. |
| `searching` | All the issues related to the Searching algorithms. |
| `sorting` | All the issues related to the Sorting algorithms. |
| `bit-operations` | Issue that are created inside the bit-operation package. |
| `string-manipulations` | All the issues that are related to the string-manipulation feature. |
| `math` | All the issues that are incorporated inside the Math package. |
| `caching` | All the issues that are related to the caching module. |

#### Pull Request Labels

| Label name | Description |
| --- | --- |
| `work-in-progress` | Pull requests which are still being worked on, more changes will follow. |
| `needs-review` | Pull requests which need code review, and approval from maintainers or TPA's core team. |
| `under-review` | Pull requests being reviewed by maintainers or TPA's core team. |
| `requires-changes` | Pull requests which need to be updated based on review comments and then reviewed again. |
| `needs-testing` | Pull requests which need manual testing. |

### Connect with other contributors
<table class="tg">
  <col width="35%">
  <col width="65%">
  <tr>
    <td>Slack</td>
    <td>
      <p>
        Register for the TPA Community Slack at
	<a href="https://tpa-collaborators.slack.com/" target="_blank">https://tpa-collaborators.slack.com</a>.
        We use the #the-python-algorithm for general discussion, and there are separate channels for feature specific discussions as well.
      </p>
    </td>
  </tr>
  <tr>
    <td>Mail us</td>
    <td>
      <p>
        Contact us at <strong>the-python-algorithm@outlook.com</strong>
      </p>
    </td>
  </tr>
</table>


[good-first-issue]: https://github.com/the-python-algorithm/tpa/labels/good-first-issue
[help-wanted]: https://github.com/the-python-algorithm/tpa/labels/help-wanted
[tpa-pull-request-template]: https://github.com/the-python-algorithm/.github/tree/master/PULL_REQUEST_TEMPLATE
[tpa-contributors-guide]: docs/contributors_guide

