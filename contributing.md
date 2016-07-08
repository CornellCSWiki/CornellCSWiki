---
layout: article
title: Contributing Guide
---

This wiki is cool, right? But you know what would make it even better? Your help! This site was started by students just like you, and we need your help in keeping it up-to-date and adding new content.

* TOC
{:toc}

## You Don't Have to Write

If you're not feeling like writing, you can still help us out! Suggestions, corrections, and comments are all welcome. Just [create an issue]({{ site.repository_issues }}).

## Make a Github Account

Go to [Github](https://github.com) and sign up. You'll need to confirm your email address before you can do anything else.

Already have one? Skip down to either [Editing a Page](#editing-a-page) or [Making a New Page](#making-a-new-page).

If you're feeling overwhelmed, [create an issue]({{site.repository_issues}}) and one of us will help you out. We'd love to walk you through the process, and teach you about open source at the same time! Just tell us what you're interested in working on.

## Editing a Page

If you've heard about Git or Github and how difficult it can't be, don't worry. Github makes it easy with a web interface. Just visit our [repository]({{ site.repository }}) and find the page you want to edit. Then just hit the edit button!

<!-- TODO: add screenshot of the button. How do I/can I do this from the web interface? -->
<!-- TODO: is there some way to avoid hardcoding the repository link? Maybe use a site variable -->

Github will take care of the Git details for you—in particular, it'll automatically fork the project for you. (Curious? Check out [Forking](#forking) below.) You'll then be presented with an editor where you can make changes to your heart's content. This wiki uses Markdown formatting, which you may have heard of before. We have a quick [guide to Markdown below](#about-markdown).

## Making a New Page

Making a completely new page is pretty simple, too. Like editing a page, just visit our [repository]({{ site.repository }}) and click *New Page*. To make it easier, we have some templates you can copy:

- [Class info page template]({{ site.repository }}/blob/gh-pages/class_template.md) ([[class_template | rendered]])
- More to come!

You'll want to edit the page title at the top of the document, which looks something like this:

```yaml
---
layout: article
title: Contributing Guide
---
```

## About Markdown

[Markdown](https://daringfireball.net/projects/markdown/) is a simple way to add formatting to plain text documents. You write a document using whatever editor you want, sprinkling in \**asterisks*\* to italicize your text and __ __underscores__ __ to bold it. Some more formatting:

* Lead off with an asterisk or dash to make a list.
    * Indent a few spaces to get a nested one!
* Insert a snippet of code with `` `backticks` ``.

1. You can make numbered lists, too!
1. Markdown automatically numbers the lists for you.

And add a heading with some `## Hashtags`.

There's also some Markdown formatting specific to the software we're using for this wiki, [Jekyll](https://jekyllrb.com/). In particular, you might notice a section like this at the top of every page:

```yaml
---
layout: article
title: Contributing Guide
---
```

This is just metadata that tells Jekyll what page template to use and what the page title is.

Another addition is *wikilinks*, which let you link to a page with just the title. For example, \[\[ Home \]\] will result in [[Home]]. Using a vertical bar, you can override the title: \[\[ Home \| index \]\] will lead to [[Home|index]].

## Getting Your Changes Reviewed

At the bottom of the editor, you'll find a place to describe your changes. Github gives you two boxes: one for a short summary of the contribution, and an optional long description. Together, these make up the Git commit message. Write up a little summary of what you did, like "Added page on contributing", "Added median grade to CS 1110 Spring 2015", or "Fixed typos in CS 2112 page". Once you're done, hit "Propose new file". This will make a *pull request*, which is a fancy way of saying that Github will let us know about your changes, and we can review them before integrating them into the wiki. Github presents a summary of what you're doing—don't worry about this and just choose to "Make a pull request".

Sometimes, we might ask you to make a few changes—maybe there's a few typos, maybe there's a formatting thing, or maybe we'd like the page to be structured like other similar pages. In these cases, we'll help you with Git and Github, and teach you a little bit more about contributing to open source in the process. Most of the time, as soon as we get around to reviewing your changes, we'll just accept them.

Congratulations, you're a contributor! If you've never done this before, then even better—you've just made your first contribution to open source.

## What Next

There's always more work to be done! Take a look at our [issues]({{ site.repository_issues }}), and comment on anything you'd like to work on. We'll help you through the rest. If you're interested in the open-source aspect, read on.

### Open Source

When you make a contribution, you don't just hand off ownership of your work to us. Instead, your writing, like everything else here, will be placed under a *license*, which says what we—and you—can and cannot do with it. In our case, we're using the TODO license, which says TODO.

These licenses ultimately derive from the *free software movement*, which is about free (as in freedom) software. In short, free software means that you have the freedom to run and modify the software, and the freedom to let others run, modify, and distribute the software as well. Open source is a fork (ha!) of this movement. If you're intrigued, drop by OpenSourceCornell sometime and we'll show you what free & open source software is all about. You can also check out the [Free Software Foundation](http://www.fsf.org/), [Free Culture Foundation](http://freeculture.org/) and [Open Source Initiative](https://opensource.org/).

### Forking

What is all this Git nonsense anyways? We'll leave out the discussion of what Git is for now, but forking and pull requests are the model that Github uses for contributing. Note that what *Github* does isn't necessarily the same as what *open source projects in general* do!

In Git, all your code lives in a *repository*. A repository can be copied on Github by *forking* it. You can then modify the code however you like. When you're ready to submit your changes back to the original, *upstream* repository, you create a *pull request*. A pull request is a set of changes that you, the owner of the fork, wants to send back to the upstream repository.

## Joining the Team

As you've no doubt noticed, this is a student-run wiki. We do have some reviewing and moderation—this is just to keep out spam, and so that we can introduce people to open source/Git as well. If you're interested in working with us, drop us an [email](dml339@cornell.edu), or come find us (we hang around OpenSourceCornell, mostly).
