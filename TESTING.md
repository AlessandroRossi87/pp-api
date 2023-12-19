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

## Python Validation

All directories underwent flake8 analysis, revealing several issues related to different factors such as excessive line lengths, white spaces, indentation, and docstring concerns.

All identified issues were addressed, except for those associated with line lengths in migration files (auto-generated and left untouched).

A warning was flagged for env.py being imported but unused; however, it was disregarded since it is actively utilized in the development version.

![Comments](https://github.com/AlessandroRossi87/pp-api/blob/main/readmefiles/testcomments.png)

![Contact](https://github.com/AlessandroRossi87/pp-api/blob/main/readmefiles/testcontact.png)

![Followers](https://github.com/AlessandroRossi87/pp-api/blob/main/readmefiles/testfollowers.png)

![Plants](https://github.com/AlessandroRossi87/pp-api/blob/main/readmefiles/testplants.png)

![pp-api](https://github.com/AlessandroRossi87/pp-api/blob/main/readmefiles/testppapi.png)

![Profiles](https://github.com/AlessandroRossi87/pp-api/blob/main/readmefiles/testprofiles.png)

![Reactions](https://github.com/AlessandroRossi87/pp-api/blob/main/readmefiles/testreactions.png)

## CSS Validation

All CSS files were validated and no errors were found.

![W3C](https://github.com/AlessandroRossi87/pp-api/blob/main/readmefiles/W3Cvalidator.png)