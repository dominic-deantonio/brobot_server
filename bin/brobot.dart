import 'package:alfred/alfred.dart';

void main() async {
  final app = Alfred();

  app.all('/test', (req, res) => 'Hello World from Dart!');

  await app.listen(3000);
}