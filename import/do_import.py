#!/usr/bin/env python
for line in manifest:
    item = json.loads(line)
    VideoItem(ia_metadata=item).save()
