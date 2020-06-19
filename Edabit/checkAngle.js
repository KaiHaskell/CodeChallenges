function missingAngle(angle1, angle2) {
  //subtract the values from 180
  const angle3 = 180 - (angle1 + angle2);
  //determine the type of angle based on the result of that operation
  switch (true) {
    case angle3 < 90:
      return "acute";
    case angle3 == 90:
      return "right";
    case angle3 > 90:
      return "obtuse";
  }
}
