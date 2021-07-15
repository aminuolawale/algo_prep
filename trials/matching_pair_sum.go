package main

import "fmt"

// further test cases

func main(){
 array := []int{1, 3, 3,4}
 answer := matchingPairSum(array)
 fmt.Println(answer)
}


func matchingPairSum(array []int) string {
	fronti:= 0
	backi:=len(array) -1
	for fronti != backi {
		sum := array[fronti] + array[backi]
		if (sum == 8) {
			return "YES"
		} else if (sum >8) {
			backi --
		} else {
			fronti ++
		}
	}
	return "NO"
}