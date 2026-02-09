# Cucumber Gherkin Reference

Source: [https://cucumber.io/docs/gherkin/reference/](https://cucumber.io/docs/gherkin/reference/)

## Keywords

Each line that isn't a blank line has to start with a Gherkin keyword, followed by any text you like. The only exceptions are the free-form descriptions placed underneath Example/Scenario, Background, Scenario Outline and Rule lines.

The primary keywords are:
- [Feature](#feature)
- [Rule](#rule) (as of Gherkin 6)
- [Example](#example) (or Scenario)
- [Given](#given), [When](#when), [Then](#then), [And](#and-but), [But](#and-but) for steps (or [*](#*))
- [Background](#background)
- [Scenario Outline](#scenario-outline) (or [Scenario Template](#scenario-outline))
- [Examples](#examples) (or [Scenarios](#examples))

There are a few secondary keywords as well:
- `"""` (Doc Strings)
- `|` (Data Tables)
- `@` (Tags)
- `#` (Comments)

### Feature

The purpose of the Feature keyword is to provide a high-level description of a software feature, and to group related scenarios.

The first primary keyword in a Gherkin document must always be Feature, followed by a `:` and a short text that describes the feature.

```gherkin
Feature: Guess the word
  The word guess game is a turn-based game for two players.
  The Maker makes a word for the Breaker to guess.
  The game is over when the Breaker guesses the Maker's word.

  Example: Maker starts a game
```

### Rule

The (optional) Rule keyword has been part of Gherkin since v6.

The purpose of the Rule keyword is to represent one business rule that should be implemented. It provides additional information for a feature. A Rule is used to group together several scenarios that belong to this business rule.

### Example

This is a concrete example that illustrates a business rule. It consists of a list of steps.
The keyword `Scenario` is a synonym of the keyword `Example`.

Examples follow this same pattern:
- Describe an initial context (Given steps)
- Describe an event (When steps)
- Describe an expected outcome (Then steps)

### Steps

Each step starts with Given, When, Then, And, or But.

Cucumber executes each step in a scenario one at a time, in the sequence you’ve written them in. When Cucumber tries to execute a step, it looks for a matching step definition to execute.

#### Given

Given steps are used to describe the initial context of the system - the scene of the scenario. It is typically something that happened in the past.

#### When

When steps are used to describe an event, or an action. This can be a person interacting with the system, or it can be an event triggered by another system.

#### Then

Then steps are used to describe an expected outcome, or result. The step definition of a Then step should use an assertion to compare the actual outcome (what the system actually does) to the expected outcome (what the step says the system is supposed to do).

#### And, But

If you have successive Given's or Then's, you could write:

```gherkin
Example: Multiple Givens
  Given one thing
  And another thing
  And yet another thing
  When I open my eyes
  Then I should see something
  But I shouldn't see something else
```

### Background

Occasionally you'll find yourself repeating the same Given steps in all of the scenarios in a Feature.

Since it is repeated in every scenario, this is an indication that those steps are not essential to describe the scenarios; they are incidental details. You can literally move such Given steps to the background, by grouping them under a Background section.

A Background allows you to add some context to the scenarios that follow it. It can contain one or more Given steps, which are run before each scenario.

### Scenario Outline

The Scenario Outline keyword can be used to run the same Scenario multiple times, with different combinations of values.

The keyword `Scenario Template` is a synonym of the keyword `Scenario Outline`.

Scenario outlines allow us to more concisely express these scenarios through the use of a template with `< >`-delimited parameters:

```gherkin
Scenario Outline: eating
  Given there are <start> cucumbers
  When I eat <eat> cucumbers
  Then I should have <left> cucumbers

  Examples:
    | start | eat | left |
    | 12    | 5   | 7    |
    | 20    | 5   | 15   |
```

### Examples

A Scenario Outline must contain one or more Examples (or Scenarios) section(s). Its steps are interpreted as a template which is never directly run. Instead, the Scenario Outline is run once for each row in the Examples section beneath it (not counting the first header row).

## Step Arguments

In some cases you might want to pass more data to a step than fits on a single line. For this purpose Gherkin has Doc Strings and Data Tables.

### Doc Strings

Doc Strings are handy for passing a larger piece of text to a step definition. The text should be offset by delimiters consisting of three double-quote marks on lines of their own:

```gherkin
Given a blog post named "Random" with Markdown body
  """
  Some Title, Eh?
  ===============
  Here is the first paragraph of my blog post.
  Lorem ipsum dolor sit amet, consectetur adipiscing elit.
  """
```

### Data Tables

Data Tables are handy for passing a list of values to a step definition:

```gherkin
Given the following users exist:
  | name   | email              | twitter         |
  | Aslak  | aslak@cucumber.io  | @aslak_hellesoy |
  | Julien | julien@cucumber.io | @jbpros         |
  | Matt   | matt@cucumber.io   | @mattwynne      |
```
