# ffmpeg_cut

## description

A ffmpeg wrapper to quickly cut video file.


## Usage

./ffmpeg_cut.py start_time end_time file

Instead of `ffmpeg -i file.mp4 -ss 00:00:03 -t 00:00:08 -async 1 -c copy file_0001.mp4` with `-t` is the duration you have to compute, you can just put the start and end time like this :
`ffmpeg 00:00:03 00:00:11 file.mp4`

The output filename is automatically generate to not erase existing files.

## License

[WTFP](LICENSE.txt)
