# author : Amit Malaker date: 8/2/22
import random
import os
import shutil
import click
import tqdm

@click.command
@click.option('--input', default='', help='Name of the input folder')
@click.option('--output', default='', help='Name of the input folder')
@click.option('--size', default=0, help='Name of the input folder')
@click.option('--seed', default=0, help='Name of the input folder')
def main(input, output, size, seed):
    if input=='':
        click.BadOptionUsage('--input', 'Must be some valid name')
    if output=='':
        click.BadOptionUsage('--output', 'Must be some valid name')
    if size==0:
        click.BadOptionUsage('--size', 'Must be greater than one')
    if not seed==0:
        random.seed(seed)
    files = os.listdir(input)
    sample = random.sample(range(0, len(files)), size)
    for idx in sample:
        os.makedirs(output, exist_ok=True)
        shutil.copy(os.path.join(input, files[idx]), os.path.join(output, files[idx]))


if __name__=='__main__':
    main()
