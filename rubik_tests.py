
from unittest import main, TestCase
from rubik import makeCube, rotate, rotateFace, makeFace

class TestRubik (TestCase) :

    def test_rotate_face(self) :
        face = makeFace(3, 'W')
        face[0][0] = 'B'
        face[0][1] = 'O'
        face[1][1] = 'Y'
        # B O W
        # W Y W
        # W W W
        self.assertEqual(rotateFace(face, False),
                [
                    ['W','W','B'],
                    ['W','Y','O'],
                    ['W','W','W']
                    ])

    def test_rotate_face_inverse(self) :
        face = makeFace(3, 'W')
        face[0][0] = 'B'
        face[0][1] = 'O'
        face[1][1] = 'Y'
        # B O W
        # W Y W
        # W W W
        self.assertEqual(rotateFace(face, True),
                [
                    ['W','W','W'],
                    ['O','Y','W'],
                    ['B','W','W']
                    ])

    def test_front_rotate(self) :
        cube = makeCube(3)
        self.assertEqual(rotate(cube,"front",False),
                    {
                        "top" : [
                            ['W','W','W'],
                            ['W','W','W'],
                            ['R','R','R']
                            ],
                        "front" : [
                            ['B','B','B'],
                            ['B','B','B'],
                            ['B','B','B']
                            ],
                        "left" : [
                            ['R','R','Y'],
                            ['R','R','Y'],
                            ['R','R','Y']
                            ],
                        "back" : [
                            ['G','G','G'],
                            ['G','G','G'],
                            ['G','G','G']
                            ],
                        "right" : [
                            ['W','O','O'],
                            ['W','O','O'],
                            ['W','O','O']
                            ],
                        "bot" : [
                            ['O','O','O'],
                            ['Y','Y','Y'],
                            ['Y','Y','Y']
                            ]
                    })
    
    def test_front_rotate_inverse(self) :
        cube = makeCube(3)
        self.assertEqual(rotate(cube,"front",True),
                    {
                        "top" : [
                            ['W','W','W'],
                            ['W','W','W'],
                            ['O','O','O']
                            ],
                        "front" : [
                            ['B','B','B'],
                            ['B','B','B'],
                            ['B','B','B']
                            ],
                        "left" : [
                            ['R','R','W'],
                            ['R','R','W'],
                            ['R','R','W']
                            ],
                        "back" : [
                            ['G','G','G'],
                            ['G','G','G'],
                            ['G','G','G']
                            ],
                        "right" : [
                            ['Y','O','O'],
                            ['Y','O','O'],
                            ['Y','O','O']
                            ],
                        "bot" : [
                            ['R','R','R'],
                            ['Y','Y','Y'],
                            ['Y','Y','Y']
                            ]
                    })

if __name__ == "__main__" :
    main()
