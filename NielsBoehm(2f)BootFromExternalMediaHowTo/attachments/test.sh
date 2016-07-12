#! /bin/sh

zwei=2

level3() {
 eins=A
 zwei=B
 echo "<$eins> <$zwei> <$drei>"
}

level2() {
 local eins zwei drei=three
 level3
 echo "<$eins> <$zwei> <$drei>"
}

level1() {
 level2
 echo "<$eins> <$zwei> <$drei>"
}

level1

echo "<$eins> <$zwei> <$drei>"
