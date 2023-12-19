# Testing

The API testing was initially conducted locally in the development phase. However, the primary testing took place within the frontend repositories. To assess the real APIs, manual testing was performed by interacting with form inputs and navigating through page loads.

[Document can be viewed here](https://docs.google.com/spreadsheets/d/1Avdya5IaWtNDT0rXZPDBBcYJwow3CueCoUn-AFmWIbU/edit#gid=0)

## Plants

![Posts](https://github.com/AlessandroRossi87/pp-api/blob/main/readmefiles/plantstests.png)

## Comments

![Comments](https://github.com/AlessandroRossi87/pp-api/blob/main/readmefiles/commentstests.png)

## Contact

![Contact](https://github.com/AlessandroRossi87/pp-api/blob/main/readmefiles/contacttests.png)

## Profiles

![Profiles](https://github.com/AlessandroRossi87/pp-api/blob/main/readmefiles/profiletests.png)

## Auth

![Auth](https://github.com/AlessandroRossi87/pp-api/blob/main/readmefiles/authtests.png)

# Lighthouse Testing

Lighthouse testing revealed poor performance. While this was expected with a large number of images, it could be improved in the future by compressing images before uploading them. Unfortunately, I did not have time to implement this functionality in this iteration.

![Lighthouse](https://github.com/AlessandroRossi87/pp-api/blob/main/readmefiles/lighthouse.png)

# Validator Testing

All directories underwent flake8 analysis, revealing several issues related to different factors such as excessive line lengths, white spaces, indentation, and docstring concerns.

All identified issues were addressed, except for those associated with line lengths in migration files (auto-generated and left untouched) and the seemingly unmodifiable auth validator lines in the settings.py file, which are part of the framework code.

A warning was flagged for env.py being imported but unused; however, it was disregarded since it is actively utilized in the development version.

