import asyncio
import os
import sys


# For not importing staking_deposit here
DEFAULT_VALIDATOR_KEYS_FOLDER_NAME = 'bls_to_execution_changes'


async def main(argv):
    binary_file_path = argv[1]
    my_folder_path = os.path.join(os.getcwd(), 'TESTING_TEMP_FOLDER')
    if not os.path.exists(my_folder_path):
        os.mkdir(my_folder_path)

    if os.name == 'nt':  # Windows
        run_script_cmd = ".\\" + binary_file_path + '\deposit.exe'
    else:  # Mac or Linux
        run_script_cmd = './' + binary_file_path + '/deposit'

    cmd_args = [
        run_script_cmd,
        '--language', 'english',
        '--non_interactive',
        'generate-bls-to-execution-change',
        '--bls_to_execution_changes_folder', my_folder_path,
        '--chain', 'itxtestnet',
        '--mnemonic', '\"sister protect peanut hill ready work profit fit wish want small inflict flip member tail between sick setup bright duck morning sell paper worry\"',
        '--bls_withdrawal_credentials_list', '0x00bd0b5a34de5fb17df08410b5e615dda87caf4fb72d0aac91ce5e52fc6aa8de',
        '--validator_start_index', '0',
        '--validator_indices', '1',
        '--execution_address', '0x3434343434343434343434343434343434343434',
    ]
    proc = await asyncio.create_subprocess_shell(
        ' '.join(cmd_args),
        stdin=asyncio.subprocess.PIPE,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE,
    )
    seed_phrase = ''
    parsing = False
    async for out in proc.stdout:
        output = out.decode('utf-8').rstrip()
        if output.startswith("***Using the tool"):
            parsing = True
        elif output.startswith("This is your mnemonic"):
            parsing = True
        elif output.startswith("Please type your mnemonic"):
            parsing = False
        elif parsing:
            seed_phrase += output
            if len(seed_phrase) > 0:
                encoded_phrase = seed_phrase.encode()
                proc.stdin.write(encoded_phrase)
                proc.stdin.write(b'\n')
        print(output)

    async for out in proc.stderr:
        output = out.decode('utf-8').rstrip()
        print(f'[stderr] {output}')

    assert len(seed_phrase) > 0

    # Check files
    validator_keys_folder_path = os.path.join(my_folder_path, DEFAULT_VALIDATOR_KEYS_FOLDER_NAME)
    _, _, key_files = next(os.walk(validator_keys_folder_path))

    # Clean up
    for key_file_name in key_files:
        os.remove(os.path.join(validator_keys_folder_path, key_file_name))
    os.rmdir(validator_keys_folder_path)
    os.rmdir(my_folder_path)


if os.name == 'nt':  # Windows
    loop = asyncio.ProactorEventLoop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(main(sys.argv))
else:
    asyncio.run(main(sys.argv))
