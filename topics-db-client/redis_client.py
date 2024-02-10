import redis

if __name__ == '__main__':
    r = redis.Redis(host='localhost', port=6379, db=0)
    r.set('foo', 'bar')
    print(r.get('foo'))
    r.delete('foo')
    print(r.get('foo'))
    r.set('foo', 'bar')
    r.expire('foo', 5)
