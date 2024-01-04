# MVR Editor

A program for modifying .mvr files, according to [DIN SPEC 15800:2022](https://www.beuth.de/en/technical-rule/din-spec-15801/373968511) ([view on github](https://github.com/mvrdevelopment/spec)).

### Usage

The mvr file to edit should be placed in the `/mvr_files/` directory. A specification for editing will be uploaded soon.
The filename (excluding directories and file extension) should be set as the const `MVR_NAME` in `/data/settings.py`.
Then run `mvr_format.py` to modify the mvr file. It will be outputted as `/mvr_files/{MVR_NAME}_formatted.mvr`

`mvr_generator.py` is a deprecated test file.