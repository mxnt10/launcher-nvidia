#!/bin/bash
#
# Directory: /etc/profile.d
#

function _run_nv
{
  LIBGL_ALWAYS_SOFTWARE=1 $1
}

export -f _run_nv

# aliases
