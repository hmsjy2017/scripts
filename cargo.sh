#!/usr/bin/env bash
cat /dev/null  >  ~/.cargo/config
cat << EOF >> ~/.cargo/config
[source]

[source.mirror]
registry = "https://mirrors.sjtug.sjtu.edu.cn/git/crates.io-index/"

[source.crates-io]
replace-with = "mirror"
EOF
