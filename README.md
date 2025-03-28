# Add up time ranges

This script is for [Albert](https://albertlauncher.github.io/) to add up multiple time ranges. The result is a floating-point number of hours.

## Query format

All times are in 24h format. The time ranges consists of pairs of time strings separated by spaces. The first time sting of the pair is the start time and the second is the end time. E.g.:

`t 12:00 12:15 13:30 14:00`

The query above starts with the trigger `t ` followed by two pairs of time ranges which will be calculated and added up: `12:00` to `12:15` and `13:30` to `14:00`.

You can modify the result by a number of minutes. Just add the string `+10m` to add 10 minutes or `-12m` to subtract 12 minutes from the result.

## Installing

Clone this repo into the Albert extension folder:

```shell
git clone git@github.com:kringkaste/albert-time-addup.git ~/.local/share/albert/python/plugins/albert-time-addup
```

Restart Albert and go to the extension tab in the settings and activate the extension.