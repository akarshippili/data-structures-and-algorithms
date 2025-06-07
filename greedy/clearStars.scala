object Solution {
  def clearStars(s: String): String = {

    val ans: mutable.ListBuffer[Char] = mutable.ListBuffer.empty[Char]
    val map: mutable.Map[Char, Array[Int]] = mutable.Map.empty
    for (index <- s.indices) {
      if s(index) == '*' then {
        val record: Option[(Char, Array[Int])] = map.keys.toSeq.sorted.collectFirst { case c if !map(c).isEmpty => (c, map(c)) }
        record match {
          case Some((c, arr)) => map(c) = map(c).dropRight(1)
          case None => -1
        }
      } else {
        map(s(index)) = map.getOrElse(s(index), Array.empty[Int]) :+ index
      }

      println(s"Current character: ${s(index)}, ans: ${ans.mkString("")}, map: ${map.map { case (k, v) => s"$k -> ${v.mkString(",")}" }.mkString(", ")}")
    }

    for (index <- s.indices) {
      val ch: Char = s(index)
      if ch != '*' && !map(ch).isEmpty && map(ch).head == index then {
        ans += ch
        map(ch) = map(ch).tail
      }
    }
    ans.mkString("")
  }
}