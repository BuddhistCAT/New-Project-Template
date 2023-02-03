# HOW-TO: Segmenting

This instruction covers how to initially segment the text as part of [starting a new project](https://github.com/BuddhistCAT/New-Project-Template/blob/main/documentation/Starting-New-Project.md) as well as how to re-segment source strings once the project has already been started.

## Background

## Initial Segmenting

Initial segmenting refers to the case where as part [starting a new project](https://github.com/BuddhistCAT/New-Project-Template/blob/main/documentation/Starting-New-Project.md) one must segment the source text. 

The current best-practice is to do it manually so that each segment to be translated is on its own line/row. It can be done automatically in various ways, but this is very strongly discouraged. Having the translator initially go through the source text to be translated breaking it down to translateable segments helps the translator and the translation project in multiple ways.

## Re-Segmenting

Sometimes the need to re-segment a particular segment arises in midst of already translating the text. When this need arises, you initiate the re-segmenting by clicking `Edit Source` inside Transifex in the translation window (note you have to be project maintainer to see it, otherwise you will not see it) and then edit the strings as you like.

**In the case you want to move part of the segment to next or previous,** then simply move the part of the segment from one to another

**In the case you want to merge two segments entirely,** then simply move the content from one segment to another, and mark the now empty segment with []  (this means the now empty segment will be ignored in the publication phase)

**In the case you want to merge more than two strings entirely,** then do exactly like In the case you want to merge two strings entirely explained above.

**In the case you want to break down a segment**, mark the segment with [~] in the position you want to break it in. Make sure to mark the corresponding translated segment with [~] as well. Note that this will not result in the segment being visibly broken down into two segments inside Transifex, but the change will reflect in the publication phase. 

These three, moving content from one segment to another, merging segments entirely, and breaking segments into parts, cover all possible cases for source string formatting during the translation project. So you can consider this instruction to be conclusive pertaining to this matter.
