package solution

import (
	"bytes"
	"crypto/md5"
	"fmt"
	"io"
	"strconv"
	"strings"
)

func md5Hash(input string) string {
	hasher := md5.New()
	io.WriteString(hasher, input)
	return fmt.Sprintf("%x", hasher.Sum(nil))
}

func md5HashBytes(input string) []byte {
	hasher := md5.New()
	io.WriteString(hasher, input)
	return hasher.Sum(nil)
}

func (Solution) Day4Part1(fn string) int {
	s := toString(fn)
	suffix := 0
	for {
		f := md5Hash(s + strconv.Itoa(suffix))[:5]
		if strings.EqualFold(f, "00000") {
			return suffix
		}
		suffix++
	}
}
func (Solution) Day4Part2(fn string) int {
	s := toString(fn)
	suffix := 0
	for {
		if suffix%100000 == 0 {
			fmt.Println(suffix)
		}
		f := md5HashBytes(s + strconv.Itoa(suffix))[:3]
		if bytes.Equal(f, []byte{0, 0, 0}) {
			return suffix
		}
		suffix++
	}
}
