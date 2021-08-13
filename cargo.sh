#!/usr/bin/env bash
cat >> ~/.cargo/config <<EOF
[source]

[source.mirror]
registry = "https://mirrors.sjtug.sjtu.edu.cn/git/crates.io-index/"

[source.crates-io]
replace-with = "mirror"

EOF  
