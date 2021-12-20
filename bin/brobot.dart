import 'package:alfred/alfred.dart';

enum Dir { Stopped, Forward, Left, Right, Reverse }

void main() async {
  final app = Alfred();

  app.all('/go', (req, res) {
    final int dirIndex = int.parse(req.uri.queryParameters['d'] ?? '0');
    final Dir dir = Dir.values[dirIndex];
    print(dir);
    return dirIndex;
  });

  app.all('/status', (req, res) => 'OK');

  await app.listen(3000);
}
