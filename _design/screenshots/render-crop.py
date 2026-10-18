"""Render a proposed crop from a retained screenshot; never edit the source PNG."""
from pathlib import Path
from PIL import Image
import argparse,json

parser=argparse.ArgumentParser(description=__doc__)
parser.add_argument('--image',required=True,help='Participant image path, relative to the repository root')
parser.add_argument('--box',nargs=4,type=int,metavar=('LEFT','TOP','RIGHT','BOTTOM'))
parser.add_argument('--output',required=True,help='New preview output path')
args=parser.parse_args()
root=Path(__file__).resolve().parents[2]
manifest=json.loads((Path(__file__).parent/'manifest.json').read_text())
record=manifest['sources'].get(args.image)
if record is None:parser.error('No retained original is mapped to that participant image.')
source=root/record['source']
image=Image.open(source)
box=args.box or record['approved_crop'] or [0,0,image.width,image.height]
left,top,right,bottom=box
if not (0<=left<right<=image.width and 0<=top<bottom<=image.height):parser.error('Crop exceeds source dimensions.')
output=Path(args.output).resolve()
if output==source.resolve() or output==Path(__file__).resolve():parser.error('Choose a separate preview output file.')
if output.exists():parser.error('Output already exists; choose a new filename.')
output.parent.mkdir(parents=True,exist_ok=True)
result=image.crop(box)
result.save(output,**({'quality':94} if output.suffix.lower() in {'.jpg','.jpeg'} else {}))
print(f'Wrote {output}: {result.width} x {result.height}')
