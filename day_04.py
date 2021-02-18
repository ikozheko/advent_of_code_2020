import re


class Passport:
    byr = None
    iyr = None
    eyr = None
    hgt = None
    hcl = None
    ecl = None
    pid = None
    cid = None

    def __setitem__(self, key, value):
        if key in self.all_fields:
            setattr(self, key, value)
        else: raise ValueError

    def __getitem__(self, key):
        if key in self.all_fields:
            return getattr(self, key, None)
        else: raise ValueError

    required_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    all_fields = required_fields + ['cid']

    def is_valid_byr(self):
        if self.byr is None:
            return False, 'BYR missed'
        v = int(self.byr)
        if v < 1920 or v > 2002:
            return False, 'constraint=[between 1920 and 2002]'
        return True

    def is_valid_iyr(self):
        if self.iyr is None:
            return False, 'IYR missed'
        v = int(self.iyr)
        if v < 2010 or v > 2020:
            return False, 'constraint=[between 2010 and 2020]'
        return True

    def is_valid_eyr(self):
        if self.eyr is None:
            return False, 'EYR missed'
        v = int(self.eyr)
        if v < 2020 or v > 2030:
            return False, 'constraint=[between 2020 and 2030]'
        return True

    def is_valid_hgt(self):
        v = self.hgt
        if v is None:
            return False, 'Height must be specified'

        m = re.match('^(\d+)(cm|in)$', v)
        if not m:
            return False, f'{v} XXXX constraint=[d+(cm|in)]'
        v, u = m[1], m[2]
        if v is None:
            return False, 'Height value is not specified'
        v = int(v)
        if u == 'cm':
            if v < 150 or v > 193:
                return False, 'height in cm constraint=[between 150 and 193]]'
            return True
        elif u == 'in':
            if v < 59 or v > 76:
                return False, 'height in in constraint=[between 59 and 76]'
            return True
        else:
            return False, 'Unknown height unit'

    def is_valid_hcl(self):
        v = self.hcl
        if v is None:
            return False, 'HCL must be specified'
        if not re.match('^#[0-9a-f]{6}$', v):
            return False, 'invalid hcl format'
        return True

    def is_valid_ecl(self):
        v = self.ecl
        if v is None:
            return False, 'ECL must be specified'
        if not re.match('^(amb|blu|brn|gry|grn|hzl|oth)$', v):
            return False, 'ECL must be in [amb|blu|brn|gry|grn|hzl|oth]'
        return True

    def is_valid_pid(self):
        v = self.pid
        try:
            if v is None or not re.match('(\d){9}', v):
                return False, 'pid must be a 9-number'
            return True
        except TypeError as e:
            print(e)
            print(self.pid)

    def is_valid_cid(self):
        return True

    def validate(self):
        errors = []
        for f in self.all_fields:
            validator = getattr(self, f'is_valid_{f}')
            res = validator()
            if type(res) == tuple:
                is_correct, error_msg = res
            else:
                if res:
                    continue
            if is_correct:
                continue
            else:
                errors.append({
                    'field': f,
                    'value': self[f],
                    'error_msg': error_msg,
                })
        return errors

    def __str__(self):
        return f'Passport#{self.pid}'


def passport_generator():
    with open('input.txt', 'r') as f:
        obj = Passport()
        for line in f:
            if line != '\n':
                pairs = line.strip().split(' ')
                for pair in pairs:
                    k, v = pair.split(':')
                    obj[k] = v
            else:
                yield obj
                obj = Passport()


total = 0
count_of_valid = 0
has_invalid_passports = False
stop_on_error = False

for p in passport_generator():
    total += 1
    errors = p.validate()
    s = str(p)
    if len(errors) > 0:
        s += f' has {len(errors)} errors:'
        print(s)
        for e in errors:
            print(e['field'] + ' => ' + e['error_msg'])
        has_invalid_passports = True
        if stop_on_error:
            break
    else:
        count_of_valid += 1

print(f'\n\ttotal = {total}')
print(f'\tcount of valid = {count_of_valid}')










































