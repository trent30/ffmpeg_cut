# ffmpeg_cut

## description

A ffmpeg wrapper to quickly cut video file.


## Usage

python ffmpeg_cut.py start_time end_time file

Instead of `ffmpeg -i file.mp4 -ss 00:00:03 -t 00:00:08 -async 1 -c copy file_0001.mp4` with `-t` is the duration you have to compute, you can just put the start and end time like this :
`python ffmpeg_cut.py 3 11 file.mp4`

The output filename is automatically generate to not erase existing files.
The left zero are not mandatory, `1:42` means 1 minute and 42 seconds.

## License

[WTFP](LICENSE.txt)
