# Leame Mucho

## Hackforms (A hacky survey for researchers with zero plata)

Doing online surveys is expensive
(did you know that Survey Monleys asks for a yearly payment in order to randomize pages in a form?).
This script simply randomizes requests to a preset list of google forms. Easy and hacky way to
randomize pages in a form.

Google Sheets is able to randomize questions.

This allows for a somewhat randomized survey.

## Why was this created?

I needed users to evaluate multiple songs using a web form. The user to song assignment needed
to be random. Users could evaluate more than one song.

## How to use?

1. Create copies of the same form just changing whatever is needed per copy
    - For example, if you need users to tag images, create one form per image
    - If you need users to rate songs, create one form per song
1. Change the list of URLs in the Python File
1. Make sure your form accepts only one answer per email
1. I recommend collecting emails
1. Add a link to the URL of the website at the end of the form. This way, users can rate other items.

## The hacky bit

A cookie keeps track of which forms users saw. This + collecting e-mails and setting one answer
per form make's sure there are no repeat answers. 
