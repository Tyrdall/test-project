# Django test

This test will help you assess and improve your skills in the areas of Django, APIs and UI.

## Context

Day by day journalists are flooded with a huge amount of textual information from various sources. As it is incredibly time consuming to view and categorize each text manually, an automatic categorization by news topic should be implemented. This way journalists should be able to filter the vast amounts by topic to reduce the information to relevant topics only.
It is planned to stick to a standardized taxonomy – the IPTC Mediatopics: https://cv.iptc.org/newscodes/mediatopic/. Textrazor offers an API to automatically extract the relevant topics from a given text document that seem to be well suited for the use case.
A small tool should be provided to easily test the quality of the API with some of the journalists. The tool should provide a text field to paste any given text. After pressing a button the text should be analyzed by Textrazor and the returned mediatopics clearly displayed on the website.

## Technologies to be used

- Python incl. all available libraries and frameworks
- JavaScript incl. all available libraries and frameworks
- HTML
- CSS/SASS/SCSS

## Task

- Create a fork of this repository
- Get a test account at https://www.textrazor.com/
- Create a page, which shows a very simple form with just one text field and a submit button
- If the form is submitted, the content of the text field should be sent to the TextRazor API (https://www.textrazor.com/docs/python) to receive topics
- Display the given topics of TextRazor in the template

## Requirements

- You have a week to do this
- Use the already created Django project

## Notes

- There is no sample solution here
- First and foremost, functionality and clean code are important
